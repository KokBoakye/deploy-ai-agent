terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  backend "s3" {
    bucket = "ai-agent-terraform-state-02-02-2026"
    key    = "ai-agent/terraform.tfstate"
    region = "us-east-1"
  }
}
