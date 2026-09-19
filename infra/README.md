# Infrastructure as Code

Proxmox VMs managed via Terraform, configured via Ansible.

## Prerequisites

- **Terraform** >= 1.5 (`brew install terraform`)
- **Ansible** >= 8 (`pip install ansible`)
- **Proxmox API** access (user: `root@pam`)
- **Tailscale** account + auth key
- **Ubuntu 22.04 template** in Proxmox (for VM cloning)

## Quick Start

### 1. Prepare Proxmox

Create an Ubuntu 22.04 VM template:

```bash
# On Proxmox host
qm create 9000 --name "ubuntu-22-04-template" --memory 4096 --cores 2
qm importdisk 9000 ubuntu-22.04.iso local-lvm
qm set 9000 --scsihw virtio-scsi-single --scsi0 local-lvm:vm-9000-disk-0
qm set 9000 --boot c --bootdisk scsi0
qm set 9000 --serial0 socket --vga serial0
qm template 9000
```

### 2. Configure Terraform

```bash
cd infra
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars with your Proxmox credentials
```

### 3. Provision VMs

```bash
terraform init
terraform apply
```

This creates:
- **app-server** (16GB RAM, 80GB root + 50GB data + 2GB Tailscale)
- **gitlab-server** (8GB RAM, 60GB root + 100GB data + 2GB Tailscale)

### 4. Install Ansible Collections

```bash
cd ../ansible
ansible-galaxy collection install -r requirements.yml
```

### 5. Update Inventory

Edit `ansible/hosts` with the actual IPs from Terraform output:

```ini
[app_server]
app-server ansible_host=<app-server-ip>

[gitlab_server]
gitlab-server ansible_host=<gitlab-server-ip>
```

### 6. Run Ansible

```bash
ansible-playbook site.yml
```

This installs:
- Docker on both VMs
- Tailscale on both VMs (with persistent state disk)
- App server: data disk mount, Git clone, Docker Compose stack
- GitLab server: data disk mount, GitLab Docker container

## Recreating a VM

```bash
cd infra
terraform apply
# VM is recreated, data disks are preserved
ansible-playbook site.yml
# Software is reinstalled, data is intact
```

## Tailscale MagicDNS

After setup, reach VMs by name from anywhere on your tailnet:

```
app-server.tailnet.ts.net    → Docker Compose stack
gitlab-server.tailnet.ts.net → GitLab CE
```

## Disk Layout

### App Server
| Disk | Size | Purpose | Persistent? |
|---|---|---|---|
| /dev/sda | 80GB | OS + app code | No (Terraform managed) |
| /dev/sdb | 50GB | PostgreSQL, Redis, Airflow data | Yes |
| /dev/sdc | 2GB | Tailscale state | Yes |

### GitLab Server
| Disk | Size | Purpose | Persistent? |
|---|---|---|---|
| /dev/sda | 60GB | OS + GitLab code | No (Terraform managed) |
| /dev/sdb | 100GB | GitLab data (repos, configs) | Yes |
| /dev/sdc | 2GB | Tailscale state | Yes |