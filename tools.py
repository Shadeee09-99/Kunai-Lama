import os
import sys
import time
import random
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

# Fungsi untuk membersihkan layar
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# Fungsi Animasi Loading Bar
def loading_animation(text, duration=2):
    print(f"{Fore.CYAN}[*] {text}", end="", flush=True)
    for _ in range(20):
        time.sleep(duration / 20)
        print(f"{Fore.GREEN}█", end="", flush=True)
    print(f" {Fore.GREEN}100% COMPLETE!")
    time.sleep(0.5)

# Fungsi Banner ASCII
def show_banner():
    clear_screen()
    # Ganti teks di dalam print dengan ASCII art buatanmu atau generator
    banner = f"""
{Fore.RED}  ██████╗ ██╗   ██╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
{Fore.RED}  ██╔══██╗╚██╗ ██╔╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
{Fore.YELLOW}  ██████╔╝ ╚████╔╝        ██║   ██║   ██║██║   ██║██║     ███████╗
{Fore.YELLOW}  ██╔═══╝   ╚██╔╝         ██║   ██║   ██║██║   ██║██║     ╚════██║
{Fore.GREEN}  ██║        ██║          ██║   ╚██████╔╝╚██████╔╝███████╗███████║
{Fore.GREEN}  ╚═╝        ╚═╝          ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
    """
    print(banner)
    print(f"{Fore.CYAN}  ===============================================================")
    print(f"{Fore.WHITE}  [+] Tool Created By : {Fore.YELLOW}NamaKamu")
    print(f"{Fore.WHITE}  [+] Version         : {Fore.GREEN}v1.0.0")
    print(f"{Fore.WHITE}  [+] Github          : {Fore.BLUE}github.com/usernamekamu")
    print(f"{Fore.CYAN}  ===============================================================")
    print()

# Fitur 1: Dummy (Bisa diganti isinya nanti)
def fitur_satu():
    clear_screen()
    print(f"{Fore.CYAN}[*] Menjalankan Fitur Satu...")
    loading_animation("Memuat modul rahasia", 1.5)
    print(f"\n{Fore.GREEN}[✓] Fitur Satu berhasil dijalankan!")
    print(f"{Fore.YELLOW}[!] (Kamu bisa menambahkan kode Python-mu di dalam fungsi ini)")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali ke menu...")

# Fitur 2: Matrix Effect / Animasi Hacker
def fitur_matriks():
    clear_screen()
    print(f"{Fore.GREEN}Menjalankan Animasi Matrix (Tekan CTRL+C untuk berhenti)")
    time.sleep(1)
    try:
        chars = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while True:
            line = "".join(random.choice(chars) for _ in range(50))
            print(f"{Fore.GREEN}{line}")
            time.sleep(0.05)
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Animasi dihentikan.")
        time.sleep(1)

# Fitur 3: Info Sistem
def fitur_info():
    clear_screen()
    print(f"{Fore.CYAN}==== [ SYSTEM INFO ] ====")
    os.system("uname -a")
    os.system("df -h | grep -v tmpfs")
    print(f"{Fore.CYAN}=========================")
    input(f"\n{Fore.WHITE}Tekan Enter untuk kembali ke menu...")

# Menu Utama
def main_menu():
    while True:
        show_banner()
        print(f"{Fore.RED}[01] {Fore.WHITE}Fitur Dummy 1")
        print(f"{Fore.RED}[02] {Fore.WHITE}Matrix Effect (Animasi)")
        print(f"{Fore.RED}[03] {Fore.WHITE}System Information")
        print(f"{Fore.RED}[00] {Fore.WHITE}Exit")
        print(f"{Fore.CYAN}---------------------------------------------------------------")
        
        try:
            pilihan = input(f"{Fore.GREEN}SELECT [01-03 / 00] >> {Fore.WHITE}")
            
            if pilihan == '1' or pilihan == '01':
                fitur_satu()
            elif pilihan == '2' or pilihan == '02':
                fitur_matriks()
            elif pilihan == '3' or pilihan == '03':
                fitur_info()
            elif pilihan == '0' or pilihan == '00':
                print(f"\n{Fore.RED}[!] Keluar dari program...")
                time.sleep(1)
                sys.exit()
            else:
                print(f"{Fore.RED}[!] Pilihan tidak valid! Silakan coba lagi.")
                time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[!] Program dihentikan paksa.")
            sys.exit()

# Eksekusi Program
if __name__ == "__main__":
    try:
        main_menu()
    except Exception as e:
        print(f"{Fore.RED}Terjadi kesalahan: {e}")
