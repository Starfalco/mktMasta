terraform {
  required_providers {
    proxmox = {
      source  = "telmate/proxmox"
      version = ">= 3.0.0"
    }
  }
}

provider "proxmox" {
  pm_api_url      = var.proxmox_api_url
  pm_user         = var.proxmox_api_user
  pm_password     = var.proxmox_api_password
  pm_tls_insecure = true
}

# =============================================================================
# Variables
# =============================================================================

variable "proxmox_api_url" {
  description = "Proxmox API URL"
  type        = string
  default     = "https://<proxmox-ip>:8006/api2/json"
}

variable "proxmox_api_user" {
  description = "Proxmox API user (e.g. root@pam)"
  type        = string
  default     = "root@pam"
}

variable "proxmox_api_password" {
  description = "Proxmox API password"
  type        = string
  sensitive   = true
}

variable "vm_password" {
  description = "SSH password for VMs"
  type        = string
  sensitive   = true
}

variable "ssh_public_key" {
  description = "SSH public key for VM access"
  type        = string
}

variable "tailscale_auth_key" {
  description = "Tailscale auth key for automatic node registration"
  type        = string
  sensitive   = true
}

variable "tailscale_subnet_router" {
  description = "Enable subnet router (allows other devices on tailnet to reach VMs)"
  type        = bool
  default     = false
}

variable "proxmox_node" {
  description = "Proxmox node name"
  type        = string
  default     = "pve"
}

variable "proxmox_storage" {
  description = "Proxmox storage pool for disks"
  type        = string
  default     = "local-lvm"
}

variable "vm_network_bridge" {
  description = "Network bridge for VMs"
  type        = string
  default     = "vmbr0"
}

variable "vm_gateway" {
  description = "Network gateway"
  type        = string
  default     = "192.168.1.1"
}

variable "vm_dns" {
  description = "DNS server"
  type        = string
  default     = "192.168.1.1"
}

# =============================================================================
# App Server VM
# =============================================================================

resource "proxmox_vm_qemu" "app_server" {
  name        = "app-server"
  target_node = var.proxmox_node
  os_type     = "cloud-init"
  clone       = "ubuntu-22-04-template"  # Update with your template name
  cores       = 4
  sockets     = 1
  cpu         = "host"
  memory      = 16384
  scsihw      = "virtio-scsi-single"
  agent       = 1

  # Root disk — destroyed with VM
  disk {
    size    = "80G"
    type    = "scsi"
    storage = var.proxmox_storage
  }

  # Persistent data disk (PostgreSQL, Redis, Airflow metadata)
  disk {
    size    = "50G"
    type    = "scsi"
    storage = var.proxmox_storage
    ssd     = 1
  }

  # Persistent Tailscale state disk
  disk {
    size    = "2G"
    type    = "scsi"
    storage = var.proxmox_storage
  }

  network {
    model  = "virtio"
    bridge = var.vm_network_bridge
  }

  cloudinit_disk {
    storage = var.proxmox_storage
    size    = "4G"
  }

  ipconfig0 = "ip=192.168.1.10/24,gw=192.168.1.1"
  nameserver = var.vm_dns
  ciuser     = "ubuntu"
  cipassword = var.vm_password
  sshkeys    = var.ssh_public_key

  # User-data script for cloud-init
  user_data = <<EOF
#cloud-config
hostname: app-server
fqdn: app-server.tailnet.ts.net
users:
  - name: ubuntu
    ssh_authorized_keys:
      - ${var.ssh_public_key}
    sudo: ALL=(ALL) NOPASSWD:ALL
    shell: /bin/bash
runcmd:
  - curl -fsSL https://get.docker.com | sh
  - usermod -aG docker ubuntu
  - systemctl enable docker
EOF

  lifecycle {
    ignore_changes = [
      attached_disk,
    ]
  }
}

# =============================================================================
# GitLab Server VM
# =============================================================================

resource "proxmox_vm_qemu" "gitlab_server" {
  name        = "gitlab-server"
  target_node = var.proxmox_node
  os_type     = "cloud-init"
  clone       = "ubuntu-22-04-template"  # Update with your template name
  cores       = 4
  sockets     = 1
  cpu         = "host"
  memory      = 8192
  scsihw      = "virtio-scsi-single"
  agent       = 1

  # Root disk — destroyed with VM
  disk {
    size    = "60G"
    type    = "scsi"
    storage = var.proxmox_storage
  }

  # Persistent data disk (GitLab data)
  disk {
    size    = "100G"
    type    = "scsi"
    storage = var.proxmox_storage
    ssd     = 1
  }

  # Persistent Tailscale state disk
  disk {
    size    = "2G"
    type    = "scsi"
    storage = var.proxmox_storage
  }

  network {
    model  = "virtio"
    bridge = var.vm_network_bridge
  }

  cloudinit_disk {
    storage = var.proxmox_storage
    size    = "4G"
  }

  ipconfig0 = "ip=192.168.1.11/24,gw=192.168.1.1"
  nameserver = var.vm_dns
  ciuser     = "ubuntu"
  cipassword = var.vm_password
  sshkeys    = var.ssh_public_key

  user_data = <<EOF
#cloud-init
hostname: gitlab-server
fqdn: gitlab-server.tailnet.ts.net
users:
  - name: ubuntu
    ssh_authorized_keys:
      - ${var.ssh_public_key}
    sudo: ALL=(ALL) NOPASSWD:ALL
    shell: /bin/bash
runcmd:
  - curl -fsSL https://get.docker.com | sh
  - usermod -aG docker ubuntu
  - systemctl enable docker
EOF

  lifecycle {
    ignore_changes = [
      attached_disk,
    ]
  }
}

# =============================================================================
# Outputs
# =============================================================================

output "app_server_ip" {
  description = "App server internal IP"
  value       = proxmox_vm_qemu.app_server.default_ipv4_address
}

output "app_server_tailscale_ip" {
  description = "App server Tailscale IP"
  value       = "app-server.tailnet.ts.net"
}

output "gitlab_server_ip" {
  description = "GitLab server internal IP"
  value       = proxmox_vm_qemu.gitlab_server.default_ipv4_address
}

output "gitlab_server_tailscale_ip" {
  description = "GitLab server Tailscale IP"
  value       = "gitlab-server.tailnet.ts.net"
}