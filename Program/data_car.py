from database import connect_db
from rent_return import rent_car

def data_car(nama_renter):
    """Menampilkan daftar mobil & menangani penyewaan."""  
    while True:
        print("\n=== MENU DATA MOBIL ===")               
        print("1. Tampilkan semua mobil")               
        print("2. Cari mobil berdasarkan plat nomor")
        print("3. Cari mobil berdasarkan merek")
        print("4. Kembali ke menu utama")
        
        check_mobil = input("\nPilih opsi (1-4): ").strip()

        if check_mobil == '1':
            tampilkan_semua_mobil()
            proses_penyewaan(nama_renter)

        elif check_mobil == '2':
            cari_mobil_berdasarkan_plat(nama_renter)

        elif check_mobil == '3':
            cari_mobil_berdasarkan_merek(nama_renter)

        elif check_mobil == '4':
            break  

        else:
            print("Pilihan tidak valid, silakan coba lagi.")

def tampilkan_semua_mobil():
    """Menampilkan semua mobil beserta statusnya."""
    db = connect_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT c.plat_nomor, c.merek, c.model, c.tahun, c.harga_sewa_per_hari, 
               (SELECT COUNT(*) FROM rentals WHERE rentals.plat_nomor = c.plat_nomor) AS disewa
        FROM cars c
    """)
    cars = cursor.fetchall()

    print("\n=== DAFTAR MOBIL ===")
    for car in cars:
        status = "Disewa" if car["disewa"] > 0 else "Tersedia"
        print(f"{car['plat_nomor']}: {car['merek']} {car['model']} ({car['tahun']}), Harga Sewa: {car['harga_sewa_per_hari']} Rupiah. Status: {status}")

    cursor.close()
    db.close()

def cari_mobil_berdasarkan_plat(nama_renter):
    """Mencari mobil berdasarkan plat nomor dan menampilkan status."""
    db = connect_db()
    cursor = db.cursor(dictionary=True)

    plat = input("\nMasukkan nomor plat mobil: ").upper().strip()
    
    cursor.execute("""
        SELECT c.plat_nomor, c.merek, c.model, c.tahun, c.harga_sewa_per_hari, 
               (SELECT COUNT(*) FROM rentals WHERE rentals.plat_nomor = c.plat_nomor) AS disewa
        FROM cars c WHERE c.plat_nomor = %s
    """, (plat,))
    
    car = cursor.fetchone()

    if car:
        status = "Disewa" if car["disewa"] > 0 else "Tersedia"
        print(f"\n{car['plat_nomor']}: {car['merek']} {car['model']} ({car['tahun']}), Harga Sewa: {car['harga_sewa_per_hari']} Rupiah. Status: {status}")
        proses_penyewaan(nama_renter, car["plat_nomor"])
    else:
        print("Mobil yang Anda cari tidak ditemukan.")

    cursor.close()
    db.close()

def cari_mobil_berdasarkan_merek(nama_renter):
    """Mencari mobil berdasarkan merek dan menampilkan status."""
    db = connect_db()
    cursor = db.cursor(dictionary=True)

    merek = input("\nMasukkan merek mobil: ").capitalize().strip()
    
    cursor.execute("""
        SELECT c.plat_nomor, c.merek, c.model, c.tahun, c.harga_sewa_per_hari, 
               (SELECT COUNT(*) FROM rentals WHERE rentals.plat_nomor = c.plat_nomor) AS disewa
        FROM cars c WHERE c.merek = %s
    """, (merek,))
    
    cars = cursor.fetchall()

    if cars:
        for car in cars:
            status = "Disewa" if car["disewa"] > 0 else "Tersedia"
            print(f"\n{car['plat_nomor']}: {car['merek']} {car['model']} ({car['tahun']}), Harga Sewa: {car['harga_sewa_per_hari']} Rupiah. Status: {status}")
        proses_penyewaan(nama_renter)
    else:
        print("Mobil dengan merek tersebut tidak ditemukan.")

    cursor.close()
    db.close()

def proses_penyewaan(nama_renter, plat=None):
    """Menangani proses penyewaan mobil."""
    rent_input = input("\nApakah Anda ingin menyewa mobil? (Y/N): ").upper().strip()
    
    if rent_input == 'Y':
        if not plat:
            plat = input("\nMasukkan plat nomor mobil yang ingin disewa: ").upper().strip()

        print(rent_car(nama_renter, plat))
    elif rent_input == 'N':
        return
    else:
        print("Input tidak valid! Harap masukkan 'Y' atau 'N'.")
