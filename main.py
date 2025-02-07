# ===================================
# [Your Program Title]
# ===================================
# Developed by. Jawed Iqbal Alfaruqiy

# /************************************/

# /===== Imported file =====/
import sign_menu from sign_menu

# /===== Data Model =====/
# Create your data model here
# t for tes drive
renter_acc = {'td' : 'td'}  # Dictionary untuk menyimpan data mobil. Key = ID, Values = Password
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

# /===== Main Program =====/
# Create your main program here

def  main_menu():
    """Function for Main menu
    """
    while True:
        print("\n=== MENU UTAMA ===")        
        print("1. Data mobil yang tersedia dan sewa Mobil")
        print("2. Kembalikan Mobil")
        print("3. Kembali ke menu masuk")
        print("4. Exit")

        choice = input("Pilih opsi 1-4: ")
        if choice == '1':
            pass
        if choice == '2':
            pass
        if choice == '3':
            print("Kembali ke menu masuk")
            pass
        if choice == '4':
            break

if __name__ == "__main__":
    main_menu()