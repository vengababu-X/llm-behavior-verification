def detect_drift(baseline, current, threshold=0.1):
    mean_base = sum(baseline) / len(baseline)
    mean_curr = sum(current) / len(current)

    diff = abs(mean_base - mean_curr)
    return diff > threshold, diff
