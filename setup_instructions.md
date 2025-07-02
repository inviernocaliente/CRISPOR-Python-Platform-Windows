# Setup Instructions for CRISPOR-Python-Platform

## Install WSL (Windows Subsystem for Linux) in **Powershell**

```bash

#In Command Prompt
wsl --install

```

## Install Ubuntu 24.04.1 LTS 
Install from the Microsoft Store

# Launch Ubuntu command prompt
1. Create a username and password: Follow the prompts to create a local Ubuntu user account and set a password.
2. Update packages: Run the following code in the Ubuntu terminal to update all software packages.
```bash
#In Ubuntu
sudo apt update
sudo apt upgrade -y
```

## 📦 Install Python Dependencies (in ** Windows Command Prompt** or WSL)

```bash

#In Command Prompt
pip install selenium pandas openpyxl xlrd mysql-connector-python argparse
curl -O http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/twoBitToFa
chmod +x twoBitToFa
