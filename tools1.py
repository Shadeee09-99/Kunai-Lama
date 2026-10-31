import os
import time
from colorama import Fore, Style, init

# Inisialisasi warna
init(autoreset=True)

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

if __name__ == "__main__":
    clear_screen()
    
    print(f"""{Fore.MAGENTA}
    =====================================
         [ TOOLS 1 - IP TRACKER ]
    =====================================
    """)
    
    print(f"{Fore.CYAN}[*] Menghubungkan ke modul Shell...")
    time.sleep(1)
    
    # ==========================================
    # INI DIA CARA MANGGIL FILE .SH NYA BANG
    # ==========================================
    os.system("bash ipscript.sh")
    
    # Setelah script .sh selesai/exit, program akan lanjut ke baris ini
    print(f"\n{Fore.GREEN}[✓] Kembali dari IP Tracker.")
    input(f"{Fore.YELLOW}Tekan Enter untuk kembali ke Menu Utama...")
