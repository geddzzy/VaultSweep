import subprocess

def check_firewall_status():
    try:
        output = subprocess.check_output(["netsh", "advfirewall", "show", "allprofiles"], text=True)
        if "State ON" in output or "ON" in output:
            return "Enabled"
        elif "State OFF" in output or "OFF" in output:
            return "Disabled"
        else:
            return "Unknown"
    except Exception as e:
        return f"Error checking firewall: {e}"
