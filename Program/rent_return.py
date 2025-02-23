from database import connect_db

def rent_car(nama_renter: str, plat_nomor: str) -> str:
    """Menyewa mobil berdasarkan plat_nomor nomor dengan validasi dari database."""
    
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    # Cek apakah mobil ada di database
    cursor.execute("SELECT * FROM cars WHERE plat_nomor = %s", (plat_nomor,))
    car = cursor.fetchone()

    if not car:
        cursor.close()
        conn.close()
        return "\nMobil tidak ditemukan."

    # Cek apakah pengguna sudah menyewa mobil lain
    cursor.execute("SELECT * FROM rentals WHERE renter_nama = %s", (nama_renter,))
    existing_rental = cursor.fetchone()

    if existing_rental:
        cursor.close()
        conn.close()
        return "\nAnda sudah menyewa mobil lain. Kembalikan dulu sebelum menyewa yang baru."

    # Cek apakah mobil sudah disewa orang lain
    cursor.execute("SELECT * FROM rentals WHERE plat_nomor = %s", (plat_nomor,))
    rented_car = cursor.fetchone()

    if rented_car:
        cursor.close()
        conn.close()
        return "\nMobil ini sudah disewa oleh pengguna lain."

    # Input jumlah hari sewa
    rented_day = input("Masukkan jumlah hari (angka): ").strip()
    
    if not rented_day.isdigit():
        cursor.close()
        conn.close()
        return "\nMasukkan jumlah hari dalam bentuk angka."
    
    rented_day = int(rented_day)

    # Lakukan penyewaan
    cursor.execute(
        "INSERT INTO rentals (renter_nama, plat_nomor, hari) VALUES (%s, %s, %s)",
        (nama_renter, plat_nomor, rented_day)
    )
    conn.commit()

    cursor.close()
    conn.close()

    return f"\n{plat_nomor} berhasil disewa oleh {nama_renter}, selama {rented_day} hari."


def return_car(nama_renter: str, plat_nomor: str) -> str:
    """Mengembalikan mobil yang disewa dari database."""
    
    conn = connect_db()
    cursor = conn.cursor()

    # Cek apakah pengguna sedang menyewa mobil yang ingin dikembalikan
    cursor.execute("SELECT * FROM rentals WHERE renter_nama = %s AND plat_nomor = %s", (nama_renter, plat_nomor))
    rental = cursor.fetchone()

    if not rental:
        cursor.close()
        conn.close()
        return "\nMobil tidak sedang disewa."

    # Hapus data penyewaan dari database (mobil dikembalikan)
    cursor.execute("DELETE FROM rentals WHERE renter_nama = %s AND plat_nomor = %s", (nama_renter, plat_nomor))
    conn.commit()

    cursor.close()
    conn.close()

    return f"\n{plat_nomor} berhasil dikembalikan."
