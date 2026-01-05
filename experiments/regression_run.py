import yaml
from core.llm_client import call_llm
from core.sampler import sample_responses
from drift.hypothesis_tests import detect_drift

# Dummy similarity scores for illustration
baseline_scores = [0.72, 0.75, 0.73, 0.74]
current_scores = [0.61, 0.63, 0.60, 0.62]

with open("config/thresholds.yaml") as f:
    alpha = yaml.safe_load(f)["drift"]["alpha"]

drifted, p_value = detect_drift(baseline_scores, current_scores, alpha)

if drifted:
    raise AssertionError(f"Behavior drift detected (p={p_value})")
