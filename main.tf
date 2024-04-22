provider "azurerm" {
  features {}
  skip_provider_registration = true
}

resource "azurerm_public_ip" "myvmip" {
  name                = "my-public-ip"
  location            = "francecentral"
  resource_group_name = "ADDA84-CTP"
  allocation_method   = "Static" 
}

resource "azurerm_network_interface" "myvmnic" {
  name                = "devops-20200510"
  location            = "francecentral"
  resource_group_name = "ADDA84-CTP"

  ip_configuration {
    name                          = "myNicConfiguration"
    subnet_id                     = azurerm_subnet.internal.id 
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.myvmip.id
  }
}

resource "azurerm_linux_virtual_machine" "myvm" {
  name                = "devops-20200510"
  location            = "francecentral"
  resource_group_name = "ADDA84-CTP"
  size                = "Standard_D2s_v3"
  admin_username      = "devops"
  network_interface_ids = [
    azurerm_network_interface.myvmnic.id,
  ]

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer = "0001-com-ubuntu-server-jammy"
    sku = "22_04-lts-gen2"
    version   = "latest"
  }

  admin_ssh_key {
    username   = "devops"
    public_key = file("~/.ssh/id_rsa.pub")
  }
}