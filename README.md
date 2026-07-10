# Verifiable Roof Evidence Package

Public-safe source-spine snapshot for Verifiable Roof(TM).

Evidence date: 2026-07-10  
Prepared for: Inspector Roofing and Restoration / Richard Amir Nasser  
Status: evidence package, not a legal opinion

## Current Evidence Position

Verifiable Roof(TM) has public evidence, but the wording must stay careful:

- USPTO: `VERIFIABLE ROOF` is a live service mark application, Serial No. `99910284`, filed June 28, 2026, awaiting examination as of the TSDR status generated July 10, 2026.
- Zenodo: public DOI records already mention Verifiable Roof, including `10.5281/zenodo.21042531`, `10.5281/zenodo.21013082`, and `10.5281/zenodo.21045292`.
- GitHub: existing public source-spine repositories reference Verifiable Roof, including `RichNass87/inspector-roofing-atlas-query-intelligence` and `RichNass87/inspector-roofing-search-integrity-report`.
- Hugging Face: the Atlas dataset and demo Space already exist and reference the public source-spine; exact dedicated `verifiable-roof` records are still pending unless created from this package.
- Site evidence: the Inspector Roofing homepage and Atlas study page are live as of July 10, 2026; the checked `/ip/` URL redirects to the homepage.

Do not describe Verifiable Roof(TM) as a registered trademark unless the USPTO status changes. Do not use the registered trademark symbol.

## Install And Run Locally

This package works without installing anything:

```bash
python3 app.py --build-only
python3 app.py --port 7860
```

Open `http://127.0.0.1:7860/`.

If Gradio is installed, `app.py` launches an interactive Gradio app. If Gradio is not installed, it builds and serves a static evidence dashboard with the same data.

## Data Files

- `data/evidence_sources.csv`: dated source table.
- `data/claim_register.csv`: supported, unsupported, and pending claim language.
- `data/platform_records.csv`: GitHub, Hugging Face, Zenodo, USPTO, and site record status.
- `data/uspto_verifiable_roof_public_safe.json`: public-safe USPTO extract with personal contact/address fields intentionally omitted.
- `data/zenodo_records.json`: public Zenodo DOI evidence found for Verifiable Roof.
- `dataset_info.json`: Hugging Face-style dataset metadata.
- `.zenodo.json`: Zenodo-ready metadata for a future dedicated archive.

## Public-Safe Claim Rules

Allowed:

- "Verifiable Roof(TM) is the subject of a live USPTO service mark application, Serial No. 99910284."
- "Existing DOI-backed public records mention Verifiable Roof(TM)."
- "The package provides a public-safe evidence map for source-spine review."

Not allowed:

- "Verifiable Roof is registered."
- "Verifiable Roof guarantees ranking, AI citations, claim approval, insurance coverage, engineering conclusions, or code compliance."
- "The public dataset includes private customer files, full photo manifests, claim documents, or personal identifiers."

## Suggested Dedicated Records

Recommended public names:

- GitHub repository: `RichNass87/verifiable-roof-evidence`
- Hugging Face dataset: `InspectorRoofing/verifiable-roof-evidence`
- Hugging Face Space: `InspectorRoofing/verifiable-roof-evidence-checker`
- Zenodo title: `Verifiable Roof Evidence Package: Public-Safe Source Spine Snapshot (2026-07-10)`

Use the files in this package as the initial public-safe release.
