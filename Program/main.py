# ===================================
# [CRUD Rental Mobil Himmel]
# ===================================
# Developed by. Jawed Iqbal Alfaruqiy

# /************************************/

# /===== Imported file =====/
from login_register import login, register
from rent_return import status_cars, return_car, renter_own, rent_car
from data_car import data_car

# ===== Sign menu program =====
def sign_menu():
    while True:
        print("\n=== MENU MASUK RENTAL MOBIL XY ===")
        print("1. Masukkan akun")
        print("2. Daftarkan akun")
        print("3. Exit") 

        option = input("Pilih opsi (1-3) : ")

        if option == '1':
            print("\n=== Masuk ===")
            print("Masukkan ID dan password")
            id_renter = input("Enter ID : ")
            pwd_renter = input("Enter password : ")
            user = login(id_renter, pwd_renter)  # Pastikan fungsi login sudah ada
            if user == "Login berhasil":  
                print("\nLogin Berhasil")
                return id_renter  # Mengembalikan ID pengguna setelah login sukses
            else:
                print(user)  # Menampilkan pesan kesalahan

        elif option == '2':
            print("\n=== Daftar ===")
            print("Daftarkan ID dan password")
            id_regis = input("Enter ID : ")
            pwd_regis = input("Enter password : ")
            user = register(id_regis, pwd_regis)  # Pastikan fungsi register sudah ada
            if user == "ID sudah ada":
                print("ID yang anda masukkan sudah ada sebelumnya")
            else:
                print(user)

        elif option == '3':
            print("\nTerima kasih telah menggunakan layanan kami!")
            exit()
        else:
            print("Input invalid")

    # return None  # Jika keluar dari sign_menu tanpa login, kembalikan None

# ===== Main menu program =====
def main_menu(id_renter):
    # if id_renter is None:
    #     print("Akses ditolak! Silakan login terlebih dahulu.")
    #     return

    while True:
        print(f"\nSelamat datang, Renter {id_renter.capitalize()}!")  # Menampilkan ID pengguna
        print("\n=== MENU UTAMA ===")        
        print("1. Data mobil yang tersedia dan sewa mobil")
        print("2. Kembalikan Mobil")
        print("3. Kembali ke menu masuk")
        print("4. Exit")

        choice = input("Pilih opsi 1-4: ")

        if choice == '1':
            data_car(status_cars, renter_own, id_renter, rent_car)

        elif choice == '2':
            print("\nMobil yang kamu pinjam : ")
            print(renter_own)
            rent_info = input("Masukkan plat nomor mobil yang ingin dikembalikan : ")
            if rent_info in status_cars:
                rented_car = return_car(id_renter, rent_info)
                print(rented_car)
            else:
                print("id tidak sesuai")

        elif choice == '3':
            print("\nKembali ke menu masuk")
            return
        
        elif choice == '4':
            print("Terima kasih telah menggunakan layanan kami!")
            exit()

        else:
            print("Input invalid")

# ===== Main Loop =====
if __name__ == "__main__":
    while True:
        id_renter = sign_menu()  # Menyimpan hasil login
        if id_renter:  # Jika login berhasil
            main_menu(id_renter)  # Masuk ke menu utama
        else:
            break