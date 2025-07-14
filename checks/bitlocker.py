import subprocess

def check_bitlocker_status():
    try:
        output = subprocess.check_output(
            ["manage-bde", "-status"],
            text=True,
            stderr=subprocess.STDOUT
        )
        if "Percentage Encrypted: 100%" in output:
            return "Protected"
        elif "Percentage Encrypted: 0%" in output:
            return "Not Protected"
        else:
            return output
    except subprocess.CalledProcessError as e:
        if "denied" in e.output:
            return "BitLocker check failed: Run as Administrator."
        else:
            return f"Error checking BitLocker: {e.output.strip()}"
    except Exception as e:
        return f"Error checking BitLocker: {e}"
