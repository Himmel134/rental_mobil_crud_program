from login_register import renters_data

def biodata_menu(nama):
    """Menampilkan biodata pengguna dan memberikan opsi edit atau hapus."""
    print("\n=== BIODATA RENTER ===")
    if nama in renters_data:
        data = renters_data[nama]
        print(f"Nama: {nama}")
        print(f"Nomor KTP: {data['ktp']}")

        print("\nOpsi:")
        print("1. Ubah Data")
        print("2. Hapus Data")
        print("3. Kembali ke Menu Utama")
        
        opsi = input("Pilih opsi (1-3): ").strip()

        if opsi == '1':
            ubah_data(nama)
        elif opsi == '2':
            hapus_data(nama)
        elif opsi == '3':
            return
        else:
            print("Opsi tidak valid! Kembali ke menu utama.")
    else:
        print("Biodata tidak ditemukan! Anda perlu mendaftar terlebih dahulu.")

def ubah_data(nama):
    """Memungkinkan pengguna untuk mengubah biodata mereka."""
    print("\n=== UBAH DATA RENTER ===")

    # Input data baru
    nama_baru = input("Masukkan Nama Baru (kosongkan jika tidak ingin mengubah): ").strip()
    ktp_baru = input("Masukkan Nomor KTP Baru (minimal 10 digit, kosongkan jika tidak ingin mengubah): ").strip()
    password_baru = input("Masukkan Password Baru (minimal 6 karakter, kosongkan jika tidak ingin mengubah): ").strip()

    # Validasi dan update data
    if nama_baru:
        renters_data[nama_baru] = renters_data.pop(nama)
        nama = nama_baru

    if ktp_baru:
        if not ktp_baru.isnumeric() or len(ktp_baru) < 10:
            print("Nomor KTP tidak valid! Perubahan dibatalkan.")
            return
        renters_data[nama]["ktp"] = ktp_baru

    if password_baru:
        if len(password_baru) < 6:
            print("Password terlalu pendek! Perubahan dibatalkan.")
            return
        renters_data[nama]["password"] = password_baru

    print("Data berhasil diperbarui!")

def hapus_data(nama):
    """Menghapus data renter dari sistem."""
    konfirmasi = input("Apakah Anda yakin ingin menghapus biodata? (y/n): ").strip().lower()
    if konfirmasi == 'y':
        del renters_data[nama]
        print("Biodata berhasil dihapus! Kembali ke menu utama.")
    else:
        print("Penghapusan dibatalkan.")
