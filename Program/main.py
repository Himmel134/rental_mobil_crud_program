# ===================================
# [CRUD Rental Mobil Himmel]
# ===================================
# Developed by. Jawed Iqbal Alfaruqiy

# /************************************/

from login_register import login, register
from data_car import data_car
from rent_return import rent_car, return_car
from biodata import biodata_menu

def sign_menu():
    while True:
        print("\n=== MENU MASUK RENTAL MOBIL ===")
        print("1. Masukkan akun")
        print("2. Daftarkan akun")
        print("3. Exit") 

        option = input("Pilih opsi (1-3): ").strip()

        if option == '1':
            nama = input("Masukkan Nama: ").strip().title()
            pwd = input("Masukkan Password: ").strip()
            user = login(nama, pwd)  

            if user == "Login berhasil":  
                print("\nLogin Berhasil!")
                main_menu(nama)
            else:
                print(user)

        elif option == '2':
            nama = input("Masukkan Nama Lengkap: ").strip().title()
            # ktp = input("Masukkan Nomor KTP: ").strip()
            pwd = input("Masukkan Password: ").strip()
            print(register(nama, pwd))

        elif option == '3':
            print("\nTerima kasih telah menggunakan layanan kami!")
            exit()

def main_menu(nama):
    while True:
        print(f"\nSelamat datang, {nama}!")  
        print("\n=== MENU UTAMA ===")        
        print("1. Data mobil yang tersedia dan sewa mobil")
        print("2. Kembalikan Mobil")
        print("3. Biodata renter")
        print("4. Exit")

        choice = input("Pilih opsi (1-4): ").strip()

        if choice == '1':
            data_car(nama, rent_car)  # Menampilkan daftar mobil dan menangani penyewaan

        elif choice == '2':
            plat = input("Masukkan plat nomor mobil yang ingin dikembalikan: ").strip()
            print(return_car(nama, plat))

        elif choice == '3':
            biodata_menu(nama)

        elif choice == '4':
            print("\nKeluar dari sistem.")
            exit()
        else:
            print("input invalid")

if __name__ == "__main__":
    sign_menu()
