resource "azurerm_network_interface" "main" {
  name                = "unique-SALAH"
  location            = "francecentral"
  resource_group_name = var.resource_group_name

  ip_configuration {
    name                          = "internal-SALAH"
    subnet_id                     = data.azurerm_subnet.existing.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.main.id
  }
}

resource "azurerm_public_ip" "main" {
  name                = "unique-pub-SALAH"
  location            = "francecentral"
  resource_group_name = var.resource_group_name
  allocation_method   = "Dynamic"
}