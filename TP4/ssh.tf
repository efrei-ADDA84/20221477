resource "tls_private_key" "ssh" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

output "private_key_pem" {
  value     = tls_private_key.ssh.private_key_pem
  sensitive = true
}

output "public_key_openssh" {
  value = tls_private_key.ssh.public_key_openssh
}