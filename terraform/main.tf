# 1. Tell Terraform we are using AWS
provider "aws" {
  region = "us-east-1" 
}

# 2. Create the ECR Repository for our Docker images
resource "aws_ecr_repository" "app_repo" {
  name                 = "django-security-app"
  image_tag_mutability = "MUTABLE"

  # We can even enable AWS's built-in basic scanning here!
  image_scanning_configuration {
    scan_on_push = true
  }
}

# 3. Create the S3 Bucket for our security scan reports
resource "aws_s3_bucket" "security_reports" {
  # S3 bucket names MUST be globally unique across all of AWS. 
  # Using your GitHub username helps ensure this name is available.
  bucket = "devops-security-reports-abhiii265" 
}