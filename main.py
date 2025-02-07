# ===================================
# [CRUD Rental Mobil Himmel]
# ===================================
# Developed by. Jawed Iqbal Alfaruqiy

# /************************************/

# /===== Imported file =====/
from login_register import login, register
from rent_return import status_cars, rented_cars, rent_car, return_car

# ===== Sign menu program =====
def sign_menu():
    while True:
        print("\n=== RENTAL MOBIL HIMMEL ===")
        print("1. Masuk")
        print("2. Daftar")
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
        print(f"\nSelamat datang, {id_renter.capitalize()}!")  # Menampilkan ID pengguna
        print("\n=== MENU UTAMA ===")        
        print("1. Data mobil yang tersedia dan sewa Mobil")
        print("2. Kembalikan Mobil")
        print("3. Kembali ke menu masuk")
        print("4. Exit")

        choice = input("Pilih opsi 1-4: ")

        if choice == '1':
            print("\nMobil yang tersedia")
        # Cek Ketersediaan mobil
            for car_num, car_info in status_cars.items():    
                status = "Disewa" if car_num in rented_cars else "Tersedia"
                print(f"{car_num}: {car_info['merek']} {car_info['model']} ({car_info['tahun']}), Harga Sewa: {car_info['harga_sewa_per_hari']} Rupiah. Status: {status}")
            
            want_rent = input("\nApakah anda ingin menyewa (Y/N): ")
            if want_rent.upper() == 'Y':
                car_id = input("\nMasukkan ID mobil yang ingin disewa : ").lower()
                car_id = rent_car(car_id)
            elif want_rent.upper() == 'N':
                continue
            else:
                print("Harap masukkan input dengan benar")
        
        elif choice == '2':
            car_id = input("Masukkan ID mobil yang ingin dikembalikan : ")
            car_id = return_car(car_id)
            print(car_id)
            
        elif choice == '3':
            print("Kembali ke menu masuk")
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