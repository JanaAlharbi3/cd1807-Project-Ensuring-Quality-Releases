resource "azurerm_public_ip" "test" {
  name                = "${var.application_type}-publicip-pubip"
  location            = var.location
  resource_group_name = var.resource_group
  sku                 = "Standard"
  allocation_method   = "Static"    # <-- required for Standard
  tags                = var.tags
}
