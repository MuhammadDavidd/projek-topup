import requests
import time
import os

def clear_screen():
    os.system('clear')

def main_menu():
    while True:
        clear_screen()
        print("=" * 35)
        print("       🔍 LOKASI TRACKER MENU       ")
        print("=" * 35)
        print("[1] 🚀 Run Location Script")
        print("[2] ❌ Exit")
        print("[3] 👤 Credits")
        print("[4] 🔄 Refresh Menu")
        print("=" * 35)

        choice = input("Pilih opsi (1-4): ")

        if choice == "1":
            run_script()
        elif choice == "2":
            print("Terima kasih telah menggunakan program ini!")
            time.sleep(1)
            break
        elif choice == "3":
            show_credits()
        elif choice == "4":
            print("Merefresh menu...")
            time.sleep(1)
        else:
            print("Pilihan tidak valid. Coba lagi.")
            time.sleep(1)

def run_script():
    clear_screen()
    print("Menjalankan script lokasi...")
    try:
        # Mengambil data lokasi dari API ipinfo.io
        response = requests.get("https://ipinfo.io")
        data = response.json()

        # Menampilkan hasil lokasi
        print("=== 📍 Lokasi Terdeteksi ===")
        print(f"Kota: {data.get('city', 'Tidak Diketahui')}")
        print(f"Wilayah: {data.get('region', 'Tidak Diketahui')}")
        print(f"Negara: {data.get('country', 'Tidak Diketahui')}")
        print(f"Lokasi (Latitude, Longitude): {data.get('loc', 'Tidak Diketahui')}")
        print(f"ISP: {data.get('org', 'Tidak Diketahui')}")
        print("============================")
    except Exception as e:
        print("Gagal mendeteksi lokasi. Periksa koneksi internet.")
        print("Error:", e)
    input("\nTekan Enter untuk kembali ke menu...")

def show_credits():
    clear_screen()
    print("=== 👤 Credits ===")
    print("Script dibuat oleh Muhammad David Aryanto (davidcuy@contact.me")
    print("Versi: 1.0")
    print("Terima kasih telah menggunakan script ini!")
    print("==================")
    input("\nTekan Enter untuk kembali ke menu...")

# Menjalankan menu utama
main_menu()
