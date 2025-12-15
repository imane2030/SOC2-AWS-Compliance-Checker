import boto3

def check_cloudtrail_enabled():
    client = boto3.client("cloudtrail")
    trails = client.describe_trails(includeShadowTrails=False)["trailList"]
    findings = []

    if not trails:
        findings.append(("GLOBAL", "FAIL", "No CloudTrail trails configured"))
        return findings

    for trail in trails:
        name = trail["Name"]
        status = client.get_trail_status(Name=name)
        if status.get("IsLogging"):
            findings.append((name, "PASS", "CloudTrail logging enabled"))
        else:
            findings.append((name, "FAIL", "Trail exists but logging disabled"))

    return findings
