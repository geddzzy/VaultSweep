from scanner import VaultSweepScanner

def print_banner():
    print(
        r"""
__     __          _ _   ____                         
\ \   / /_ _ _   _| | |_/ ___|_      _____  ___ _ __  
 \ \ / / _` | | | | | __\___ \ \ /\ / / _ \/ _ \ '_ \ 
  \ V / (_| | |_| | | |_ ___) \ V  V /  __/  __/ |_) |
   \_/ \__,_|\__,_|_|\__|____/ \_/\_/ \___|\___| .__/ 
                                               |_|    
"""
    )

def main():
    print_banner()
    scanner = VaultSweepScanner()
    scanner.run_all_checks()
    scanner.generate_report()

if __name__ == "__main__":
    main()
