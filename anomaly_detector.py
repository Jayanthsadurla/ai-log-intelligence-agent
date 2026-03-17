def detect_anomaly(log):
    error_keywords = ["error", "failed", "exception", "timeout"]

    for word in error_keywords:
        if word.lower() in log.lower():
            return True

    return False