import platform
import wmi
from checks import firewall, bitlocker
from report import Report


class VaultSweepScanner:
    def __init__(self):
        self.wmi_conn = wmi.WMI()
        self.results = {}

    def gather_system_info(self):
        self.results["OS"] = platform.platform()
        self.results["Hostname"] = platform.node()
        self.results["Processor"] = platform.processor()
        # Add more info if needed

    def check_firewall(self):
        fw_status = firewall.check_firewall_status()
        self.results["Firewall Status"] = fw_status

    def check_bitlocker(self):
        bl_status = bitlocker.check_bitlocker_status()
        self.results["BitLocker Status"] = bl_status

    def run_all_checks(self):
        print("[*] Gathering system information...")
        self.gather_system_info()
        print("[*] Checking firewall status...")
        self.check_firewall()
        print("[*] Checking BitLocker status...")
        self.check_bitlocker()

    def generate_report(self):
        report = Report(self.results)
        report.print_report()
        report.save_report("vaultsweep_report.txt")
