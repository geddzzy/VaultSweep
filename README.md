# VaultSweep – Windows Vulnerability Scanner

```
__     __          _ _   ____                         
\ \   / /_ _ _   _| | |_/ ___|_      _____  ___ _ __  
 \ \ / / _` | | | | | __\___ \ \ /\ / / _ \/ _ \ '_ \ 
  \ V / (_| | |_| | | |_ ___) \ V  V /  __/  __/ |_) |
   \_/ \__,_|\__,_|_|\__|____/ \_/\_/ \___|\___| .__/ 
                                               |_|    
```


VaultSweep is a Python tool that scans Windows systems for common security vulnerabilities and configuration issues. It helps users identify risks such as disabled firewalls, unencrypted drives, and missing security updates, generating actionable reports to improve system security.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/vaultsweep.git
cd vaultsweep
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the scanner with:

```bash
python vaultsweep.py
```

VaultSweep will output a vulnerability scan report to the console and save it as `vaultsweep_report.txt` in the current directory.

## Project Structure
```
vaultsweep/
├── checks/
│   ├── bitlocker.py
│   └── firewall.py
├── __init__.py
├── report.py
├── requirements.txt
├── scanner.py
├── vaultsweep.py
├── LICENSE
├── README.md
└── .gitignore
```
- vaultsweep.py – Main entry point (or use main.py if you prefer)
- scanner.py – Core scanning logic
- report.py – Report generation
- checks/ – Individual vulnerability checks (e.g., firewall, bitlocker)
- requirements.txt – Python dependencies
- .gitignore – Files and folders to exclude from git
- README.md – This file!

## Features

- Collects system information (OS, hostname, processor)
- Checks Windows Firewall status
- Checks BitLocker encryption status
- Modular design for easy extension
- Generates detailed text reports

## About

Created by a security engineer to learn, share, and demonstrate practical Python and cybersecurity skills.  
Feel free to use, contribute, or fork for your own learning!


## Acknowledgments

- Uses the `wmi` Python library for Windows Management Instrumentation queries.
- Inspired by common Windows security best practices and vulnerability scanning tools.


## Contributing

Contributions are welcome! Please open an issue or submit a pull request.


## License

This project is licensed under the MIT License.

**Author:** geddzzy 

**Copyright ©** 2025 geddzzy

All rights reserved.
