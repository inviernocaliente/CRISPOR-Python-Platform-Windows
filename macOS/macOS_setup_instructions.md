# Setup Instructions for CRISPOR-Python-Platform

## Install Python 3
1) Open your terminal and instal Homebrew
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
2) Install Python
```bash
brew install python
```
  -> This will (a) install the latest python version (b) give you python3 command and (c) give you pip3 command for installing packages 


Download the [scripts folder](scripts) 
This folder contains all of the Python files needed to run this program. 

## Navigate to this scripts folder on macOS Command Prompt
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

## Install Python Dependencies 
Make sure that you are downloading this in your scripts folder!
```bash
#In Terminal
curl -O http://hgdownload.soe.ucsc.edu/admin/exe/macOSX.x86_64/twoBitToFa 
chmod +x twoBitToFa
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

## Extract the Fasta (.fa) file
### This will allow you to obtain a specific sequence of the genome (the intended gene) to later subit to CRISPOR. Look at [getFasta.py] for the code


