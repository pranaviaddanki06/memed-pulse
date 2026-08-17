# Model Card

## Purpose
Estimate a prototype *relative attention potential* for demonstration content, not future views.

## Data and evaluation
The 300-row dataset is synthetic and deliberately correlated. Offline sklearn evaluation is reproducible through `ml/training/train.py`; UI metrics are clearly labeled prototype metrics. No private or platform engagement data is used.

## Limitations and ethics
Scores can encode assumptions in the synthetic generator and should never drive high-stakes decisions. Cultural relevance is context dependent. Human review, representative real data, and bias evaluation are required before any production use.
