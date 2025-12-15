# SOC2-AWS-Compliance-Checker

Python script that automatically checks AWS accounts for SOC 2 compliance gaps and generates detailed reports mapping findings to SOC 2 Trust Service Criteria.

## Overview

This tool automates SOC 2 compliance auditing for AWS infrastructure by checking:
- **S3 Encryption (CC6.1)**: Verifies all S3 buckets have default encryption enabled
- **CloudTrail Logging (CC7.2)**: Ensures CloudTrail is configured and actively logging
- **IAM MFA Requirements (CC6.3)**: Checks that console users have MFA enabled
- **Security Group Configuration (CC6.6)**: Identifies overly permissive security groups
- **EBS Encryption (CC6.1)**: Validates EBS volumes are encrypted at rest

## Project Structure

```
SOC2-AWS-Compliance-Checker/
├── README.md
├── requirements.txt
├── soc2_controls.yaml
├── aws_checks/
│   ├── __init__.py
│   ├── s3.py
│   ├── cloudtrail.py
│   ├── iam.py
│   └── ec2.py
├── main.py
└── report.py
```

## Installation

```bash
# Clone the repository
git clone https://github.com/imane2030/SOC2-AWS-Compliance-Checker.git
cd SOC2-AWS-Compliance-Checker

# Install dependencies
pip install -r requirements.txt

# Configure AWS credentials
aws configure
```

## Usage

```bash
python main.py
```

The script will:
1. Connect to your AWS account using your configured credentials
2. Run all compliance checks
3. Generate a `soc2_report.md` file with findings

## Sample Output

```markdown
| Check ID           | SOC 2 | Resource        | Status | Control Description                          | Detail                                  |
|--------------------|-------|-----------------|--------|----------------------------------------------|-----------------------------------------|
| S3_ENCRYPTION      | CC6.1 | my-bucket       | FAIL   | S3 buckets must enforce encryption at rest   | No default encryption configured        |
| CLOUDTRAIL_ENABLED | CC7.2 | default-trail   | PASS   | CloudTrail enabled in all regions            | CloudTrail logging enabled              |
| MFA_FOR_IAM_USERS  | CC6.3 | admin-user      | FAIL   | MFA enabled for IAM console users            | Console user without MFA                |
```

## SOC 2 Control Mapping

All checks are mapped to specific SOC 2 Trust Service Criteria:

- **CC6.1** - Logical and Physical Access Controls
- **CC6.3** - Multi-Factor Authentication  
- **CC6.6** - Least Privilege Access
- **CC7.2** - System Monitoring and Logging

## Requirements

- Python 3.7+
- AWS CLI configured with appropriate credentials
- IAM permissions to read:
  - S3 bucket configurations
  - CloudTrail status
  - IAM user details
  - EC2/EBS configurations
  - Security group rules

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

## Author

Imane Errayes - [imanologya.substack.com](https://imanologya.substack.com)

---

**Note**: This is an educational project demonstrating automated compliance checking. Always review and validate compliance requirements with qualified auditors.
