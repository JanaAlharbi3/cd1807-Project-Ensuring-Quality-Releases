# Resource Group/Location
variable "location" {}
variable "resource_group" {}
variable "tags" {
  type    = map(string)
  default = {}
}
variable "application_type" {}
variable "resource_type" {}
