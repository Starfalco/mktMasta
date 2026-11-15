variable "vpc_cidr" {
  description = "VPC CIDR block"
  type        = string
  default     = "10.0.0.0/16"
}

variable "public_subnet_cidr" {
  description = "Public subnet CIDR block"
  type        = string
  default     = "10.0.1.0/24"
}

variable "private_subnet_cidr" {
  description = "Private subnet A CIDR block"
  type        = string
  default     = "10.0.2.0/24"
}

variable "private_subnet_cidr_b" {
  description = "Private subnet B CIDR block"
  type        = string
  default     = "10.0.3.0/24"
}

variable "db_name" {
  description = "PostgreSQL database name"
  type        = string
  default     = "mktmasta"
}

variable "db_username" {
  description = "PostgreSQL database username"
  type        = string
  default     = "mktmasta"
}

variable "db_password" {
  description = "PostgreSQL database password"
  type        = string
  sensitive   = true
}
