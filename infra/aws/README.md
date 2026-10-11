# AWS Infrastructure — MKTmasta

Terraform configuration for deploying MKTmasta on AWS.

## Prerequisites

- **Terraform** >= 1.5 (`brew install terraform`)
- **AWS CLI** >= 2 (`brew install awscli`)
- **AWS Account** with active subscription
- **IAM User** with `AdministratorAccess` policy
- **SSH Key Pair** named `mktmasta-key` in AWS (eu-west-3 region)

## Setup

### 1. Configure AWS Credentials

```bash
aws configure
# Enter Access Key ID and Secret Access Key
# Default region: eu-west-3
```

### 2. Create SSH Key Pair in AWS

```bash
aws ec2 create-key-pair \
  --key-name mktmasta-key \
  --region eu-west-3 \
  --query 'KeyMaterial' \
  --output text > ~/.ssh/mktmasta-key.pem

chmod 400 ~/.ssh/mktmasta-key.pem
```

### 3. Configure Terraform

```bash
cd infra/aws
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars with your database password
```

### 4. Apply Infrastructure

```bash
terraform init
terraform plan
terraform apply
```

This creates:
- VPC with public/private subnets
- EC2 instance (app server)
- RDS PostgreSQL (database)
- ECR repository (container registry)
- S3 bucket (backups)
- Security groups

### 5. Configure GitHub Actions

Add the following secrets to your GitHub repository:

```
AWS_ACCESS_KEY_ID     → IAM user access key
AWS_SECRET_ACCESS_KEY → IAM user secret key
AWS_REGION            → eu-west-3
ECR_REPOSITORY        → mktmasta-app
ECR_REGISTRY          → <account-id>.dkr.ecr.eu-west-3.amazonaws.com
EC2_HOST              → <ec2-public-ip>
SSH_PRIVATE_KEY       → Private key for EC2 access
```

## Destroy Infrastructure

```bash
terraform destroy
```

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│  GitHub.com (code hosting)                               │
│  └── GitHub Actions (CI/CD) + Self-hosted runners       │
└────────────────┬────────────────────────────────────────┘
                 │ SSH + docker pull
                 ↓
┌─────────────────────────────────────────────────────────┐
│  AWS EC2 (App Server)                                    │
│  ├── Angular (nginx, static)                            │
│  ├── FastAPI (REST API)                                 │
│  └── Redis (caching)                                    │
└────────────────┬────────────────────────────────────────┘
                 │
                 ↓
┌─────────────────────────────────────────────────────────┐
│  AWS RDS PostgreSQL (Production Database)                │
│  └── Screener cache, metadata, user data                │
└─────────────────────────────────────────────────────────┘
```

## Cost

| Resource | Free Tier | Cost After |
|---|---|---|
| EC2 (t3.micro) | 750 hrs/mo | ~$8/mo (t3.small) |
| RDS PostgreSQL | 20GB, 750 hrs/mo | ~$15/mo |
| ECR | 5GB | ~$0.10/mo |
| S3 | 5GB | ~$0.05/mo |
| **Total** | **$0 (6 months)** | **~$23/mo** |