# ================================
# Data Mobil & Proses Penyewaan
# ================================

def data_car(status_cars, renter_own, nama_renter, rent_car):
    """Menampilkan daftar mobil & menangani penyewaan."""
    
    while True:
        print("\n=== MENU DATA MOBIL ===")               
        print("1. Tampilkan semua mobil")               
        print("2. Cari mobil berdasarkan plat nomor")
        print("3. Cari mobil berdasarkan merek")
        print("4. Kembali ke menu utama")
        
        check_mobil = input("\nPilih opsi (1-4): ").strip()

        if check_mobil == '1':
            tampilkan_semua_mobil(status_cars, renter_own)
            proses_penyewaan(nama_renter, status_cars, renter_own, rent_car)

        elif check_mobil == '2':
            cari_mobil_berdasarkan_plat(status_cars, renter_own, nama_renter, rent_car)

        elif check_mobil == '3':
            cari_mobil_berdasarkan_merek(status_cars, renter_own, nama_renter, rent_car)

        elif check_mobil == '4':
            break  # Kembali ke menu utama

        else:
            print("Pilihan tidak valid, silakan coba lagi.")


def tampilkan_semua_mobil(status_cars, renter_own):
    """Menampilkan semua mobil beserta statusnya."""
    
    print("\n=== DAFTAR MOBIL ===")
    for plat, info in status_cars.items():
        status = "Disewa" if any(rent_info['plat mobil'] == plat for rent_info in renter_own.values()) else "Tersedia"
        print(f"{plat}: {info['merek']} {info['model']} ({info['tahun']}), Harga Sewa: {info['harga_sewa_per_hari']} Rupiah. Status: {status}")


def cari_mobil_berdasarkan_plat(status_cars, renter_own, nama_renter, rent_car):
    """Mencari mobil berdasarkan plat nomor."""
    
    plat = input("\nMasukkan nomor plat mobil: ").upper().strip()
    
    if plat in status_cars:
        info = status_cars[plat]
        status = "Disewa" if any(rent_info['plat mobil'] == plat for rent_info in renter_own.values()) else "Tersedia"
        print(f"\n{plat}: {info['merek']} {info['model']} ({info['tahun']}), Harga Sewa: {info['harga_sewa_per_hari']} Rupiah. Status: {status}")
        proses_penyewaan(nama_renter, status_cars, renter_own, rent_car, plat)
    else:
        print("Mobil yang Anda cari tidak ada.")


def cari_mobil_berdasarkan_merek(status_cars, renter_own, nama_renter, rent_car):
    """Mencari mobil berdasarkan merek."""

    merek = input("\nMasukkan merek mobil: ").capitalize().strip()
    ditemukan = False

    for plat, info in status_cars.items():
        if info["merek"] == merek:
            status = "Disewa" if any(rent_info['plat mobil'] == plat for rent_info in renter_own.values()) else "Tersedia"
            print(f"\n{plat}: {info['merek']} {info['model']} ({info['tahun']}), Harga Sewa: {info['harga_sewa_per_hari']} Rupiah. Status: {status}")
            ditemukan = True

    if ditemukan:
        proses_penyewaan(nama_renter, status_cars, renter_own, rent_car)
    else:
        print("Mobil dengan merek tersebut tidak ditemukan.")


def proses_penyewaan(nama_renter, status_cars, renter_own, rent_car, plat=None):
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
