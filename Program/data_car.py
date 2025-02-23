from database import connect_db

def data_car(nama_renter, rent_car):
    """Menampilkan daftar mobil & menangani penyewaan."""
    
    while True:
        print("\n=== MENU DATA MOBIL ===")               
        print("1. Tampilkan semua mobil")               
        print("2. Cari mobil berdasarkan plat_nomor nomor")
        print("3. Cari mobil berdasarkan merek")
        print("4. Kembali ke menu utama")
        
        check_mobil = input("\nPilih opsi (1-4): ").strip()

        if check_mobil == '1':
            tampilkan_semua_mobil()
            proses_penyewaan(nama_renter, rent_car)

        elif check_mobil == '2':
            cari_mobil_berdasarkan_plat_nomor(nama_renter, rent_car)

        elif check_mobil == '3':
            cari_mobil_berdasarkan_merek(nama_renter, rent_car)

        elif check_mobil == '4':
            break  # Kembali ke menu utama

        else:
            print("Pilihan tidak valid, silakan coba lagi.")


def tampilkan_semua_mobil():
    """Menampilkan semua mobil beserta statusnya dari database."""
    
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT c.plat_nomor, c.merek, c.model, c.tahun, c.harga_sewa_per_hari, 
        CASE 
            WHEN r.plat_nomor IS NOT NULL THEN 'Disewa' 
            ELSE 'Tersedia' 
        END AS status
        FROM cars c 
        LEFT JOIN rentals r ON c.plat_nomor = r.plat_nomor;
    """
    cursor.execute(query)
    cars = cursor.fetchall()

    print("\n=== DAFTAR MOBIL ===")
    for car in cars:
        print(f"{car['plat_nomor']}: {car['merek']} {car['model']} ({car['tahun']}), Harga Sewa: {car['harga_sewa_per_hari']} Rupiah. Status: {car['status']}")

    cursor.close()
    conn.close()


def cari_mobil_berdasarkan_plat_nomor(nama_renter, rent_car):
    """Mencari mobil berdasarkan plat_nomor nomor di database."""
    
    plat_nomor = input("\nMasukkan nomor plat_nomor mobil: ").upper().strip()

    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT c.plat_nomor, c.merek, c.model, c.tahun, c.harga_sewa_per_hari, 
        CASE 
            WHEN r.plat_nomor IS NOT NULL THEN 'Disewa' 
            ELSE 'Tersedia' 
        END AS status
        FROM cars c 
        LEFT JOIN rentals r ON c.plat_nomor = r.plat_nomor
        WHERE c.plat_nomor = %s;
    """
    cursor.execute(query, (plat_nomor,))
    car = cursor.fetchone()

    if car:
        print(f"\n{car['plat_nomor']}: {car['merek']} {car['model']} ({car['tahun']}), Harga Sewa: {car['harga_sewa_per_hari']} Rupiah. Status: {car['status']}")
        proses_penyewaan(nama_renter, rent_car, plat_nomor)
    else:
        print("Mobil yang Anda cari tidak ada.")

    cursor.close()
    conn.close()


def cari_mobil_berdasarkan_merek(nama_renter, rent_car):
    """Mencari mobil berdasarkan merek di database."""

    merek = input("\nMasukkan merek mobil: ").capitalize().strip()

    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT c.plat_nomor, c.merek, c.model, c.tahun, c.harga_sewa_per_hari, 
        CASE 
            WHEN r.plat_nomor IS NOT NULL THEN 'Disewa' 
            ELSE 'Tersedia' 
        END AS status
        FROM cars c 
        LEFT JOIN rentals r ON c.plat_nomor = r.plat_nomor
        WHERE c.merek = %s;
    """
    cursor.execute(query, (merek,))
    cars = cursor.fetchall()

    if cars:
        for car in cars:
            print(f"\n{car['plat_nomor']}: {car['merek']} {car['model']} ({car['tahun']}), Harga Sewa: {car['harga_sewa_per_hari']} Rupiah. Status: {car['status']}")
        proses_penyewaan(nama_renter, rent_car)
    else:
        print("Mobil dengan merek tersebut tidak ditemukan.")

    cursor.close()
    conn.close()


def proses_penyewaan(nama_renter, rent_car, plat_nomor=None):
    """Menangani proses penyewaan mobil."""
    
    rent_input = input("\nApakah Anda ingin menyewa mobil? (Y/N): ").upper().strip()
    
    if rent_input == 'Y':
        if not plat_nomor:
            plat_nomor = input("\nMasukkan plat_nomor nomor mobil yang ingin disewa: ").upper().strip()

        print(rent_car(nama_renter, plat_nomor))
    
    elif rent_input == 'N':
        return
    else:
        print("Input tidak valid! Harap masukkan 'Y' atau 'N'.")
