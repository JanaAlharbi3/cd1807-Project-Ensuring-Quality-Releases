# Resource Group
variable location {}
variable "resource_group" {}
variable "tags" {
  type    = map(string)
  default = {}
}

