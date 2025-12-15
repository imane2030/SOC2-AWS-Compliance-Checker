import boto3

def check_s3_encryption():
    s3 = boto3.client("s3")
    findings = []
    buckets = [b["Name"] for b in s3.list_buckets()["Buckets"]]

    for bucket in buckets:
        try:
            enc = s3.get_bucket_encryption(Bucket=bucket)
            rules = enc["ServerSideEncryptionConfiguration"]["Rules"]
            if not rules:
                findings.append((bucket, "FAIL", "No default encryption rule"))
            else:
                findings.append((bucket, "PASS", "Default encryption configured"))
        except s3.exceptions.ClientError as e:
            code = e.response["Error"]["Code"]
            if code == "ServerSideEncryptionConfigurationNotFoundError":
                findings.append((bucket, "FAIL", "No default encryption configured"))
            else:
                findings.append((bucket, "ERROR", f"Error checking encryption: {code}"))

    return findings
