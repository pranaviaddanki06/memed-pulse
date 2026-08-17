"""Run train.py first; metrics are emitted to ml/evaluation/metrics.json."""
from pathlib import Path
print(Path(__file__).with_name('metrics.json').read_text())
