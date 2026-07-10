# Verifiable Roof Evidence Package

Public-safe source-spine snapshot for Verifiable Roof(TM).

Evidence date: 2026-07-10  
Prepared for: Inspector Roofing and Restoration / Richard Amir Nasser  
Status: evidence package, not a legal opinion

## Current Evidence Position

Verifiable Roof(TM) has public evidence, but the wording must stay careful:

- USPTO: `VERIFIABLE ROOF` is a live service mark application, Serial No. `99910284`, filed June 28, 2026, awaiting examination as of the TSDR status generated July 10, 2026.
- Zenodo: the dedicated public evidence package is published at DOI `10.5281/zenodo.21298744`. Earlier DOI-backed public records also mention Verifiable Roof, including `10.5281/zenodo.21042531`, `10.5281/zenodo.21013082`, and `10.5281/zenodo.21045292`.
- GitHub: this repository is the dedicated public-safe source-spine repository for the Verifiable Roof evidence package.
- Hugging Face: the dedicated public dataset is `InspectorRoofing/verifiable-roof-evidence`.
- Wikidata: the public entity item is `Verifiable Roof`, `Q140482857`.
- Site evidence: the Inspector Roofing homepage and Atlas study page are live as of July 10, 2026; the checked `/ip/` URL redirects to the homepage.

Do not describe Verifiable Roof(TM) as a registered trademark unless the USPTO status changes. Do not use the registered trademark symbol.

## Public Records

- Verifiable Roof Wikidata item: https://www.wikidata.org/wiki/Q140482857
- Zenodo DOI: https://doi.org/10.5281/zenodo.21298744
- GitHub repository: https://github.com/RichNass87/verifiable-roof-evidence
- Hugging Face dataset: https://huggingface.co/datasets/InspectorRoofing/verifiable-roof-evidence
- USPTO TSDR record: https://tsdr.uspto.gov/statusview/sn99910284
- Richard Amir Nasser Wikidata item: https://www.wikidata.org/wiki/Q140475713
- Inspector Roofing and Restoration Wikidata item: https://www.wikidata.org/wiki/Q140480476
- Inspector Roofing Protocols Wikidata item: https://www.wikidata.org/wiki/Q140480722
- Claim Verifiability Wikidata item: https://www.wikidata.org/wiki/Q140481799

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
- `.zenodo.json`: Zenodo metadata for the public archive.

## Public-Safe Claim Rules

Allowed:

- "Verifiable Roof(TM) is the subject of a live USPTO service mark application, Serial No. 99910284."
- "The Verifiable Roof evidence package is published with DOI 10.5281/zenodo.21298744."
- "Existing DOI-backed public records mention Verifiable Roof(TM)."
- "The package provides a public-safe evidence map for source-spine review."

Not allowed:

- "Verifiable Roof is registered."
- "Verifiable Roof guarantees ranking, AI citations, claim approval, insurance coverage, engineering conclusions, or code compliance."
- "The public dataset includes private customer files, full photo manifests, claim documents, or personal identifiers."

## Dedicated Records

Public names:

- GitHub repository: `RichNass87/verifiable-roof-evidence`
- Hugging Face dataset: `InspectorRoofing/verifiable-roof-evidence`
- Hugging Face Space target: `InspectorRoofing/verifiable-roof-evidence-checker`
- Zenodo title: `Verifiable Roof Evidence Package: Public-Safe Source Spine Snapshot (2026-07-10)`
- Wikidata item: `Verifiable Roof`, `Q140482857`

Use the files in this package as the public-safe release.
