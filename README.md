# VaultSweep – Windows Vulnerability Scanner

VaultSweep is a Python tool that scans Windows systems for common security vulnerabilities and configuration issues. It helps users identify risks such as disabled firewalls, unencrypted drives, and missing security updates, generating actionable reports to improve system security.

## Features

- Collects system information (OS, hostname, processor)
- Checks Windows Firewall status
- Checks BitLocker encryption status
- Modular design for easy extension
- Generates detailed text reports

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
python main.py
```

VaultSweep will output a vulnerability scan report to the console and save it as `vaultsweep_report.txt` in the current directory.

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
