# ===================================
# [CRUD Rental Mobil Himmel]
# ===================================
# Developed by. Jawed Iqbal Alfaruqiy

# /===== Imported file =====/
from login_register import login, register
from rent_return import status_cars, return_car, renter_own, rent_car
from data_car import data_car
from biodata import biodata_menu

# ===== Sign menu program =====
def sign_menu():
    while True:
        print("\n=== MENU MASUK RENTAL MOBIL XY ===")
        print("1. Masukkan akun")
        print("2. Daftarkan akun")
        print("3. Exit") 

        option = input("Pilih opsi (1-3): ").strip()

        if option == '1':
            print("\n=== Masuk ===")
            nama = input("Masukkan Nama: ").strip()
            pwd = input("Masukkan Password: ").strip()
            user = login(nama, pwd)  

            if user == "Login berhasil":  
                print("\nLogin Berhasil!")
                return nama  # Masuk ke menu utama
            else:
                print(user)  # Menampilkan pesan kesalahan dan kembali ke menu utama

        elif option == '2':
            print("\n=== Daftar ===")
            nama = input("Masukkan Nama Lengkap: ").strip().title()
            if not nama:
                print("Nama tidak boleh kosong! Kembali ke menu utama.")
                return
            
            pwd = input("Masukkan Password (min. 6 karakter): ").strip()
            if len(pwd) < 6:
                print("Password terlalu pendek! Kembali ke menu utama.")
                return

            status = register(nama, pwd)  # Memanggil fungsi register
            print(status)  # Menampilkan pesan status (berhasil atau gagal)

        elif option == '3':
            print("\nTerima kasih telah menggunakan layanan kami!")
            exit()
        else:
            print("Input invalid! Pilih opsi 1-3.")

# ===== Main menu program =====
def main_menu(nama):
    while True:
        print(f"\nSelamat datang, {nama}!")  
        print("\n=== MENU UTAMA ===")        
        print("1. Data mobil yang tersedia dan sewa mobil")
        print("2. Kembalikan Mobil")
        print("3. Biodata renter")
        print("4. Kembali ke menu masuk")
        print("5. Exit")

        choice = input("Pilih opsi (1-5): ").strip()

        if choice == '1':
            data_car(status_cars, renter_own, nama, rent_car)

        elif choice == '2':
            print("\nMobil yang kamu pinjam:", renter_own.get(nama, "Tidak ada"))
            rent_info = input("Masukkan plat nomor mobil yang ingin dikembalikan: ").upper().strip()
            print(return_car(nama, rent_info))

        elif choice == '3':
            biodata_menu(nama)  # Pindah ke fungsi pengelolaan biodata

        elif choice == '4':
            print("\nKembali ke menu masuk...")
            return

        elif choice == '5':
            print("Terima kasih telah menggunakan layanan kami!")
            exit()

        else:
            print("Input invalid! Pilih opsi 1-5.")

# ===== Main Loop =====
if __name__ == "__main__":
    while True:
        nama = sign_menu()  
        if nama:  
            main_menu(nama)  
