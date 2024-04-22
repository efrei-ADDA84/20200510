resource "azurerm_subnet" "internal" {
  name                 = "internal"
  resource_group_name  = "ADDA84-CTP"
  virtual_network_name = "network-tp4"
  address_prefixes     = ["10.3.1.0/24"]
}