# ===================================
# [Your Program Title]
# ===================================
# Developed by. Jawed Iqbal Alfaruqiy

# /************************************/

# /===== Imported file =====/
from login_register import login, register

# /===== Data Model =====/
# Create your data model here
status_cars = {  # Dicitonary untuk mrnyimpan data mobil
    "mobil 1": {
        "merek": "Toyota",
        "model": "Avanza",
        "tahun": 2020,
        "harga_sewa_per_hari": 300_000
    },
    "mobil 2": {
        "merek": "Honda",
        "model": "Civic",
        "tahun": 2021,
        "harga_sewa_per_hari": 500_000
    },
    "mobil 3": {
        "merek": "Suzuki",
        "model": "Ertiga",
        "tahun": 2019,
        "harga_sewa_per_hari": 350_000
    }
}
rented_cars = {}  # Dictionary untuk menyimpan data mobil yang sedang disewa

# ===== Sign menu program =====
def sign_menu():
    option = None
    while option != '3':
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
            print("\nGoodbye!")
        else:
            print("Input invalid")

    # return None  # Jika keluar dari sign_menu tanpa login, kembalikan None

# ===== Main menu program =====
def main_menu(id_renter):
    # if id_renter is None:
    #     print("Akses ditolak! Silakan login terlebih dahulu.")
    #     return

    option = None
    while option != '4':
        print(f"Selamat datang, {id_renter.capitalize()}!")  # Menampilkan ID pengguna
        print("\n=== MENU UTAMA ===")        
        print("1. Data mobil yang tersedia dan sewa Mobil")
        print("2. Kembalikan Mobil")
        print("3. Kembali ke menu masuk")
        print("4. Exit")

        choice = input("Pilih opsi 1-4: ")
        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            print("Kembali ke menu masuk")
            return sign_menu()  # Kembali ke menu login
        elif choice == '4':
            print("Terima kasih telah menggunakan layanan kami!")
            break
        else:
            print("Input invalid")

if __name__ == "__main__":
    id_renter = sign_menu()  # Menyimpan hasil login
    if id_renter:  # Jika login berhasil
        main_menu(id_renter)  # Masuk ke menu utama
