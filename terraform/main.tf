terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.63.1"
    }
  }

  backend "gcs" {
    bucket = "tf-state-gdsc-ul-playground-eros"
    prefix = "terraform"
  }
}

provider "google" {
}

resource "google_compute_network" "production" {
  name                    = "production-network"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "production_us_west1" {
  region        = var.region
  ip_cidr_range = "10.0.1.0/28"
  name          = "production-us-west1"
  network       = google_compute_network.production.id
}

resource "google_compute_subnetwork" "production_us_central1" {
  region        = var.region
  ip_cidr_range = "10.0.2.0/28"
  name          = "production-us-central1"
  network       = google_compute_network.production.id
}

resource "google_compute_instance" "production" {
  name         = "production-vm"
  zone         = var.zone
  machine_type = "e2-small"

  boot_disk {
    auto_delete = true
    initialize_params {
      image = "debian-cloud/debian-11"
      size  = local.size
    }
  }

  network_interface {
    subnetwork = google_compute_subnetwork.production_us_west1.id
    access_config {
    }
  }

}

data "google_compute_instance" "development" {
  name = "development-us-west-1-c"
  zone = "us-west1-c"
}

output "gce-dev-machine-type" {
  value = data.google_compute_instance.development.machine_type
}



















