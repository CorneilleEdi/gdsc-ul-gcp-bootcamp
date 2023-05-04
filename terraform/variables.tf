variable "region" {
  type    = string
  default = "us-west1"
}


variable "zone" {
  type    = string
  default = "us-west1-b"
}

variable "mid_size" {
  type    = number
  default = 5
}

variable "users" {
  type    = list(string)
  default = ["john", "marry", "pierre"]
}

locals {
  size = var.mid_size * 2 == 15 ? 30 : 10

  users_list = [for i in var.users : replace(i, "r", "*")]
}