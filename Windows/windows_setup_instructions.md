# Setup Instructions for CRISPOR-Python-Platform

## Install WSL (Windows Subsystem for Linux) in **Powershell**

```bash

#In Command Prompt
wsl --install

```

## Install Ubuntu 24.04.1 LTS 
Install from the Microsoft Store

### Launch Windows command prompt
1. Create a username and password: Follow the prompts to create a local Ubuntu user account and set a password.
2. Update packages: Run the following code in the Windows Command Prompt to update software packages.
```bash
#In Command Prompt 
wsl sudo apt update
wsl sudo apt upgrade -y
```
## Install Python 3 and PIP (Package Installer for Python)
1. Go to Command prompt and type in the following:
```bash
#In Command Prompt
wsl sudo apt update
wsl sudo apt install python3-pip
```
2. Enter your password to your local Ubuntu user account
3. This will download both Python 3 and PIP.
   
## Download the [scripts folder](scripts) 
This folder contains all of the Python files needed to run this program. 

## Navigate to this scripts folder on Windows Command Prompt
### Basic Commands 
| task  | command |
| ------------- | ------------- |
| View Current Directory  | cd  |
| Conte  | Content Cell  |
|List files/folders | dir |
|Go into a subfolder	| cd folder_name|
|Go up one directory	| cd .. |
|Go to root of current drive	| cd \ |
|Go to a specific path	| cd "C:\Users\YourName\Documents" |
|Switch to another drive	| D: (or E: etc.) |

## Install Python Dependencies (in ** Windows Command Prompt** or WSL)
Make sure that you are downloading this in your scripts folder!
```bash
#In Command Prompt
pip install selenium pandas openpyxl xlrd mysql-connector-python argparse
curl -O http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/twoBitToFa
wsl chmod +x twoBitToFa
```

## Download the Mus Musculus (mouse) genome 
Currently, we have two versions of the Mus Musculus genome (.2bit format) ready to download, mm9 and mm10. We recommend using the mm10 gene as it is a newer version with more recent revisions.
Again, make sure that you are downloading these in your scripts folder!
1. To download mm9:
```bash
curl -O http://hgdownload.soe.ucsc.edu/goldenPath/mm9/bigZips/mm9.2bit
```
2. To download mm10:
```bash
curl -O http://hgdownload.soe.ucsc.edu/goldenPath/mm10/bigZips/mm10.2bit
```

## Run Python Program
Congratulations on setting everything up!
Fianlly, before running the program, make sure you are in the right directory on command line--- make sure that you are in the *scripts* folder.
To run the program, type in the command line:
```bash
python runAll.py -h --geneName GENENAME --genomeName GENOMENAME --genomeVers GENOMEVERS --tss TSS --lb LB --ub UB --mit MIT --doench DOENCH --offtarget OFFTARGET
```
To enter arguments, replace the parameters (shown in all caps above) with appropriate values.
Only the --geneName argument is required. The others, if no value is entered, will automatically be assigned their default value.

For more information on default values, arguments, and program usage, type the following for the help command
```bash
python runAll.py -h
```
