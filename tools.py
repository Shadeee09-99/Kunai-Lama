import os
import sys
import time
import random
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# ==========================================
# KUMPULAN ANIMASI BIAR KEREN
# ==========================================

def animasi_startup():
    clear_screen()
    # Animasi Loading Bar Start
    print(f"{Fore.CYAN}[*] Sedang Menyiapkan Environment...")
    for i in range(21):
        time.sleep(0.05)
        percent = i * 5
        bar = '█' * i + '░' * (20 - i)
        print(f"\r{Fore.GREEN}[{bar}] {percent}%", end="")
    print(f"\n{Fore.GREEN}[✓] System Ready!\n")
    time.sleep(0.5)

def animasi_typing(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animasi_pilih_menu(nama_tool):
    # Animasi muter pas milih menu
    spinner = ['|', '/', '-', '\\']
    print(f"\n{Fore.YELLOW}[*] Memuat modul {nama_tool} ", end="")
    for _ in range(15):
        for char in spinner:
            sys.stdout.write(f"\b{char}")
            sys.stdout.flush()
            time.sleep(0.05)
    print(f"\n{Fore.GREEN}[✓] Modul Siap Dieksekusi!\n")
    time.sleep(0.3)

# ==========================================
# TAMPILAN BANNER & MENU
# ==========================================

def show_banner():
    clear_screen()
    banner = f"""
{Fore.RED}  ████████╗ ██████╗  ██████╗ ██╗     ███████╗
{Fore.RED}  ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
{Fore.YELLOW}     ██║   ██║   ██║██║   ██║██║     ███████╗
{Fore.YELLOW}     ██║   ██║   ██║██║   ██║██║     ╚════██║
{Fore.GREEN}     ██║   ╚██████╔╝╚██████╔╝███████╗███████║
{Fore.GREEN}     ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
    """
    print(banner)
    print(f"{Fore.CYAN}  ==================================================")
    print(f"{Fore.WHITE}  [+] Creator : {Fore.YELLOW}Jagoan Termux")
    print(f"{Fore.WHITE}  [+] Version : {Fore.GREEN}v2.0.0 (Modular)")
    print(f"{Fore.CYAN}  ==================================================\n")

def main_menu():
    while True:
        show_banner()
        
        # Menu 1 - 10 dengan nama random
        menu_items = [
            "IP Tracker (tools1.py)",
            "Web Scanner (tools2.py)",
            "Hash Cracker (tools3.py)",
            "Network Ping (tools4.py)",
            "DNS Lookup (tools5.py)",
            "Port Scanner (tools6.py)",
            "Metadata Cleaner (tools7.py)",
            "Subdomain Finder (tools8.py)",
            "Password Generator (tools9.py)",
            "Encryptor Tools (tools10.py)"
        ]

        for i, item in enumerate(menu_items, 1):
            print(f"{Fore.RED}[{i:02d}] {Fore.WHITE}{item}")
        
        print(f"{Fore.RED}[00] {Fore.WHITE}Exit")
        print(f"{Fore.CYAN}--------------------------------------------------")
        
        try:
            pilihan = input(f"{Fore.GREEN}SELECT [01-10 / 00] >> {Fore.WHITE}")
            
            if pilihan == '0' or pilihan == '00':
                print(f"\n{Fore.RED}[!] Keluar dari program...")
                time.sleep(1)
                sys.exit()
            elif pilihan in [str(i).zfill(2) for i in range(1, 11)] or pilihan in [str(i) for i in range(1, 11)]:
                # Konversi input ke angka
                angka = int(pilihan)
                nama_file = f"tools{angka}.py"
                
                # Animasi pas milih
                animasi_pilih_menu(nama_file)
                
                # Eksekusi file terpisah
                os.system(f"python {nama_file}")
                
                # Pause sebelum balik ke menu utama
                input(f"\n{Fore.CYAN}Tekan Enter untuk kembali ke Menu Utama...")
            else:
                print(f"{Fore.RED}[!] Pilihan tidak valid! Silakan coba lagi.")
                time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[!] Program dihentikan paksa.")
            sys.exit()
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        animasi_startup() # Animasi pas python tools.py dijalanin
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Dibatalkan oleh user.")
