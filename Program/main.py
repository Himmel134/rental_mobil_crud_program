from login_register import login, register
from rent_return import return_car
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
                return nama  
            else:
                print(user)  

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

            status = register(nama, pwd)  
            print(status)  

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
            data_car(nama)

        elif choice == '2':
            return_car(nama)

        elif choice == '3':
            nama_baru = biodata_menu(nama)  # Tangkap perubahan nama
            if nama_baru:
                nama = nama_baru  # Perbarui nama di sistem

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
