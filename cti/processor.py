
scan_history = []

def analyze_ip(ip, vt_data, abuse_data):
    score = 0
    reasons = []

    # VirusTotal analysis
    if vt_data and "data" in vt_data:
        detections = vt_data["data"]["attributes"]["last_analysis_stats"]["malicious"]
        score += detections * 2
        if detections:
            reasons.append(f"VirusTotal detected {detections} malicious flags")

    # AbuseIPDB analysis
    if abuse_data and "data" in abuse_data:
        abuse_score = abuse_data["data"]["abuseConfidenceScore"]
        score += abuse_score
        if abuse_score:
            reasons.append(f"AbuseIPDB confidence: {abuse_score}")

    result = {"ip": ip, "score": score, "reasons": reasons}
    
    # Add to scan history
    scan_history.append(result)
    
    return result

