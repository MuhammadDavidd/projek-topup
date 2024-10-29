import requests
from colorama import Fore, Style, init

# Inisialisasi colorama untuk mendukung warna di Termux
init(autoreset=True)

# API Key dari OpenCage
API_KEY = "225796962c914083b79ebd419bb74681"

def deteksi_lokasi(lat, lon):
    """Fungsi untuk mendeteksi lokasi berdasarkan latitude dan longitude."""
    url = f"https://api.opencagedata.com/geocode/v1/json?q={lat}+{lon}&key={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data['results']:
            lokasi = data['results'][0]['components']
            print(f"\n{Fore.CYAN}Lokasi Terdeteksi:")
            print(f"{Fore.GREEN}- Desa/Kelurahan: {lokasi.get('village', 'Tidak Diketahui')}")
            print(f"{Fore.GREEN}- Kecamatan: {lokasi.get('suburb', 'Tidak Diketahui')}")
            print(f"{Fore.GREEN}- Kabupaten/Kota: {lokasi.get('city', 'Tidak Diketahui')}")
            print(f"{Fore.GREEN}- Provinsi: {lokasi.get('state', 'Tidak Diketahui')}")
            print(f"{Fore.GREEN}- Negara: {lokasi.get('country', 'Tidak Diketahui')}")
        else:
            print(f"{Fore.RED}Lokasi tidak ditemukan.")
    else:
        print(f"{Fore.RED}Terjadi kesalahan: {response.status_code}")

def menu():
    """Fungsi untuk menampilkan menu utama."""
    print(f"{Fore.YELLOW}===== MENU UTAMA =====")
    print(f"{Fore.MAGENTA}[1] Lanjut Cek Lokasi")
    print(f"{Fore.MAGENTA}[2] Batalkan")
    print(f"{Fore.MAGENTA}[3] Credit Pembuat")

    pilihan = input(f"\n{Fore.CYAN}Masukkan pilihan Anda: ")

    if pilihan == "1":
        latitude = input(f"{Fore.CYAN}Masukkan Latitude: ")
        longitude = input(f"{Fore.CYAN}Masukkan Longitude: ")
        deteksi_lokasi(latitude, longitude)
    elif pilihan == "2":
        print(f"{Fore.RED}Program dibatalkan.")
    elif pilihan == "3":
        print(f"\n{Fore.GREEN}Program ini dibuat oleh: Nama Anda")
    else:
        print(f"{Fore.RED}Pilihan tidak valid. Silakan coba lagi.")
        menu()

# Menjalankan menu
if __name__ == "__main__":
    menu()
