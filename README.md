# CRISPOR-Python-Platform

CRISPOR-Python-Platform is a semi-automated toolchain to design CRISPR interference (CRISPRi) guide RNAs using the UCSC Genome Browser and CRISPOR. Built with Python and Selenium, it simplifies extraction of transcription start sites (TSS), FASTA region download, and gRNA scoring.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Download](#download)
- [Set-Up & Installation](https://github.com/inviernocaliente/CRISPOR-Python-Platform-Windows/blob/main/setup_instructions.md)
- [Documentation](#documentation)

---

## Overview

This toolkit helps you:

- Identify TSS of genes from the UCSC MySQL genome database  
- Download surrounding sequences using `twoBitToFa`  
- Automate CRISPOR to design gRNAs via browser scripting  
- Convert the `.xls` download to `.csv` for easy parsing  

---

## Features

- Target gene by name (e.g. `Pou5f1`)  
- Retrieves exact genomic coordinates (strand-aware)  
- Downloads 1kb region around TSS  
- Launches Chrome, selects genome, pastes sequence, and runs CRISPOR  
- Converts CRISPOR output into `.csv`  

---

## Download

Clone the repo:
```bash
git clone https://github.com/yourusername/CRISPOR-Python-Platform.git
cd CRISPOR-Python-Platform
```

---

## Set-Up & Installation

Please choose your operating system and follow the corresponding setup instructions:

- 🪟 [Windows Setup Instructions](https://github.com/inviernocaliente/CRISPOR-Python-Platform-Windows/blob/main/Windows/windows_setup_instructions.md)
- 🍎 [macOS Setup Instructions](https://github.com/inviernocaliente/CRISPOR-Python-Platform-Windows/blob/main/macOS/macOS_setup_instructions.md)  


