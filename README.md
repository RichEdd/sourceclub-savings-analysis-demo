# Source Club Savings Analysis Demo

**Executive presentation:** see [EXECUTIVE_SUMMARY.md](EXECUTIVE_SUMMARY.md) for a hiring-ready overview, demo results, architecture, and talking points.

## Overview

This is a lightweight prototype demonstrating how Source Club could automate prospect savings analysis using:

- fuzzy product matching
- confidence scoring
- automated savings calculations
- human-in-the-loop review thresholds

This demo uses fictional dental purchasing data.

---

## Features

- Import supplier purchase history
- Compare against Source Club pricing catalog
- Match products using fuzzy logic
- Calculate estimated savings
- Flag uncertain matches for human review

---

## Tech Stack

- Python
- Pandas
- RapidFuzz

---

## Install

```bash
pip install -r requirements.txt
```

---

## Run

```bash
python main.py
```

---

## Example Output

Run `python main.py` to regenerate `output/savings_analysis_output.csv`. Thresholds in `main.py` are calibrated for this demo dataset.

| Prospect Product | Match Confidence | Workflow | Estimated Savings |
|---|---|---|---|
| Nitrile Gloves Med Blue 100ct | 83 | AUTO_APPROVED | $102.00 |
| 3M Prophy Angles Soft | 79 | MANUAL_REVIEW | $75.00 |
| Level 3 Earloop Masks 50ct | 68 | MANUAL_REVIEW | $65.70 |
| Cotton Rolls Large 200ct | 85 | MANUAL_REVIEW | $14.00 |

**Total estimated savings (demo):** $256.70

---

## Future Enhancements

- OpenAI embeddings
- vector search
- OCR support
- HubSpot integration
- human review dashboard
- AI-assisted semantic matching
