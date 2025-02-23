from database import connect_db

def biodata_menu(nama):
    """Menampilkan biodata pengguna dan memberikan opsi edit atau hapus."""
    biodata = get_biodata(nama)

    if biodata:
        print("\n=== BIODATA RENTAL ===")
        print(f"Nama: {biodata['nama']}")
        print(f"Nomor KTP: {biodata['ktp']}")

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

def get_biodata(nama):
    """Mengambil biodata renter dari database."""
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT nama, ktp FROM renters WHERE nama = %s", (nama,))
    biodata = cursor.fetchone()

    cursor.close()
    conn.close()
    return biodata

def ubah_data(nama):
    """Memungkinkan pengguna untuk mengubah biodata mereka."""
    print("\n=== UBAH DATA RENTER ===")

    conn = connect_db()
    cursor = conn.cursor()

    nama_baru = input("Masukkan Nama Baru (kosongkan jika tidak ingin mengubah): ").strip()
    ktp_baru = input("Masukkan Nomor KTP Baru (minimal 10 digit, kosongkan jika tidak ingin mengubah): ").strip()
    password_baru = input("Masukkan Password Baru (minimal 6 karakter, kosongkan jika tidak ingin mengubah): ").strip()

    if nama_baru:
        cursor.execute("UPDATE renters SET nama = %s WHERE nama = %s", (nama_baru, nama))
        nama = nama_baru  # Perbarui nama untuk query selanjutnya

    if ktp_baru:
        if not ktp_baru.isnumeric() or len(ktp_baru) < 10:
            print("Nomor KTP tidak valid! Perubahan dibatalkan.")
            cursor.close()
            conn.close()
            return
        cursor.execute("UPDATE renters SET ktp = %s WHERE nama = %s", (ktp_baru, nama))

    if password_baru:
        if len(password_baru) < 6:
            print("Password terlalu pendek! Perubahan dibatalkan.")
            cursor.close()
            conn.close()
            return
        cursor.execute("UPDATE renters SET password = %s WHERE nama = %s", (password_baru, nama))

    conn.commit()
    cursor.close()
    conn.close()
    print("Data berhasil diperbarui!")

def hapus_data(nama):
    """Menghapus data renter dari sistem."""
    konfirmasi = input("Apakah Anda yakin ingin menghapus biodata? (y/n): ").strip().lower()
    
    if konfirmasi == 'y':
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM renters WHERE nama = %s", (nama,))
        conn.commit()

        cursor.close()
        conn.close()
        print("Biodata berhasil dihapus! Kembali ke menu utama.")
    else:
        print("Penghapusan dibatalkan.")
