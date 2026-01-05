from scipy.stats import ks_2samp

def detect_drift(baseline_scores, current_scores, alpha):
    stat, p_value = ks_2samp(baseline_scores, current_scores)
    return p_value < alpha, p_value
