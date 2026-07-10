#!/usr/bin/env python3
"""Verifiable Roof evidence checker.

Runs as Gradio when available. Without Gradio, builds and serves a static
HTML dashboard using only Python's standard library.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
EXPORTS_DIR = ROOT / "exports"


def load_csv(name: str) -> List[Dict[str, str]]:
    with (DATA_DIR / name).open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def load_json(name: str):
    with (DATA_DIR / name).open(encoding="utf-8") as fh:
        return json.load(fh)


def summary() -> Dict[str, object]:
    sources = load_csv("evidence_sources.csv")
    claims = load_csv("claim_register.csv")
    platforms = load_csv("platform_records.csv")
    uspto = load_json("uspto_verifiable_roof_public_safe.json")
    zenodo = load_json("zenodo_records.json")
    return {
        "observed_on": "2026-07-10",
        "source_count": len(sources),
        "claim_count": len(claims),
        "platform_count": len(platforms),
        "uspto_status": uspto["tm5_status"],
        "uspto_serial": uspto["serial_number"],
        "zenodo_dois": [record["doi"] for record in zenodo],
        "safe_status": "Use Verifiable Roof(TM). Do not describe it as registered."
    }


def evaluate_claim(text: str) -> Dict[str, str]:
    lowered = (text or "").lower()
    if not lowered.strip():
        return {"status": "needs_input", "reason": "Enter a claim to check.", "suggested_wording": ""}
    if "registered" in lowered or "®" in text:
        return {
            "status": "unsupported",
            "reason": "USPTO TSDR shows a live application awaiting examination, not a registration.",
            "suggested_wording": "Verifiable Roof(TM) is the subject of a live USPTO service mark application, Serial No. 99910284."
        }
    if any(term in lowered for term in ["guarantee", "insurance approval", "claim approval", "engineering conclusion", "code compliance"]):
        return {
            "status": "unsupported",
            "reason": "The evidence package does not support outcome guarantees or technical/legal determinations.",
            "suggested_wording": "This package documents public source-spine evidence and claim-language boundaries."
        }
    if "pending" in lowered or "application" in lowered or "99910284" in lowered:
        return {
            "status": "supported",
            "reason": "Matches the TSDR-supported status language.",
            "suggested_wording": "Verifiable Roof(TM) is the subject of a live USPTO service mark application, Serial No. 99910284."
        }
    if "doi" in lowered or "zenodo" in lowered:
        return {
            "status": "supported_with_boundary",
            "reason": "Existing DOI records mention Verifiable Roof, but a dedicated DOI should only be claimed after publication.",
            "suggested_wording": "Existing DOI-backed public records mention Verifiable Roof(TM) as part of the Inspector Roofing source-spine."
        }
    return {
        "status": "needs_review",
        "reason": "No direct rule matched. Compare against data/claim_register.csv before publishing.",
        "suggested_wording": "Keep claims tied to dated sources and avoid guarantees."
    }


def table_html(rows: List[Dict[str, str]]) -> str:
    if not rows:
        return "<p>No rows.</p>"
    columns = list(rows[0].keys())
    head = "".join(f"<th>{html.escape(col)}</th>" for col in columns)
    body = []
    for row in rows:
        cells = "".join(f"<td>{html.escape(str(row.get(col, '')))}</td>" for col in columns)
        body.append(f"<tr>{cells}</tr>")
    return f"<table><thead><tr>{head}</tr></thead><tbody>{''.join(body)}</tbody></table>"


def build_static_dashboard() -> Path:
    EXPORTS_DIR.mkdir(exist_ok=True)
    data = summary()
    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Verifiable Roof Evidence Package</title>
<style>
body{{margin:0;font-family:Arial,Helvetica,sans-serif;color:#17202a;line-height:1.45;background:#fff}}
header{{padding:28px clamp(16px,4vw,48px);border-bottom:1px solid #d9e0e7;background:#eef5f4}}
main{{padding:24px clamp(16px,4vw,48px) 48px;max-width:1180px}}
h1{{margin:0 0 8px;font-size:clamp(28px,4vw,44px);letter-spacing:0}}
h2{{margin:28px 0 10px;font-size:22px;letter-spacing:0}}
.summary{{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:12px;margin-top:18px}}
.metric{{border:1px solid #d9e0e7;border-radius:8px;padding:14px;background:#fff}}
.metric strong{{display:block;font-size:20px;color:#0f766e}}
.notice{{border-left:4px solid #9a3412;background:#fff7ed;padding:12px 14px;max-width:880px}}
table{{border-collapse:collapse;width:100%;margin:12px 0 24px;font-size:14px}}
th,td{{border:1px solid #d9e0e7;padding:8px;vertical-align:top;text-align:left}}
th{{background:#f4f7f9}}
</style>
</head>
<body>
<header><h1>Verifiable Roof Evidence Package</h1><p>Public-safe source-spine snapshot dated {data['observed_on']}.</p></header>
<main>
<section class="summary">
<div class="metric"><strong>{data['source_count']}</strong> evidence sources</div>
<div class="metric"><strong>{data['claim_count']}</strong> claim rules</div>
<div class="metric"><strong>{data['platform_count']}</strong> platform records</div>
<div class="metric"><strong>{html.escape(str(data['uspto_serial']))}</strong> USPTO serial</div>
</section>
<h2>Boundary</h2><p class="notice">{html.escape(str(data['safe_status']))}</p>
<h2>Evidence Sources</h2>{table_html(load_csv('evidence_sources.csv'))}
<h2>Claim Register</h2>{table_html(load_csv('claim_register.csv'))}
<h2>Platform Records</h2>{table_html(load_csv('platform_records.csv'))}
</main></body></html>"""
    out = EXPORTS_DIR / "index.html"
    out.write_text(doc, encoding="utf-8")
    return out


def launch_gradio(port: int) -> bool:
    try:
        import gradio as gr  # type: ignore
    except Exception:
        return False
    with gr.Blocks(title="Verifiable Roof Evidence Package") as demo:
        gr.Markdown("# Verifiable Roof Evidence Package")
        gr.JSON(summary(), label="Evidence Summary")
        with gr.Tab("Claim Checker"):
            text = gr.Textbox(label="Claim to check", lines=3)
            result = gr.JSON(label="Result")
            gr.Button("Check Claim").click(evaluate_claim, inputs=text, outputs=result)
        with gr.Tab("Evidence Sources"):
            gr.Dataframe(value=load_csv("evidence_sources.csv"), interactive=False)
        with gr.Tab("Claim Register"):
            gr.Dataframe(value=load_csv("claim_register.csv"), interactive=False)
        with gr.Tab("Platform Records"):
            gr.Dataframe(value=load_csv("platform_records.csv"), interactive=False)
    demo.launch(server_name="0.0.0.0", server_port=port)
    return True


def serve_static(port: int) -> None:
    build_static_dashboard()
    os.chdir(EXPORTS_DIR)
    server = ThreadingHTTPServer(("127.0.0.1", port), SimpleHTTPRequestHandler)
    print(f"Serving static dashboard at http://127.0.0.1:{port}/")
    server.serve_forever()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=int(os.environ.get("PORT", "7860")))
    parser.add_argument("--build-only", action="store_true")
    args = parser.parse_args()
    out = build_static_dashboard()
    print(f"Built static dashboard: {out}")
    if args.build_only:
        print(json.dumps(summary(), indent=2))
        return
    if not launch_gradio(args.port):
        serve_static(args.port)


if __name__ == "__main__":
    main()
