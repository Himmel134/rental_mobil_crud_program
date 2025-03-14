from database import connect_db
from datetime import datetime, timedelta

def rent_car(nama_renter: str, car_id: str) -> str:
    """Menyewa mobil berdasarkan plat nomor dan menyimpan waktu serta tanggal pengembalian."""
    db = connect_db()
    cursor = db.cursor()

    # Cek apakah penyewa sudah menyewa mobil lain
    cursor.execute("""
        SELECT r.id FROM rentals r
        JOIN renters re ON r.renter_id = re.id
        WHERE re.nama = %s
    """, (nama_renter,))
    if cursor.fetchone():
        return "\nAnda sudah menyewa mobil lain. Kembalikan dulu sebelum menyewa yang baru."

    # Cek apakah mobil sudah disewa oleh orang lain
    cursor.execute("SELECT * FROM rentals WHERE plat_nomor = %s", (car_id,))
    if cursor.fetchone():
        return "\nMobil ini sudah disewa oleh pengguna lain."

    rented_day = input("Masukkan jumlah hari (angka): ").strip()

    if not rented_day.isdigit():
        return "\nMasukkan jumlah hari dalam bentuk angka."

    rented_day = int(rented_day)
    tanggal_sewa = datetime.now()
    tanggal_kembali = tanggal_sewa + timedelta(days=rented_day)

    # Ambil ID penyewa
    cursor.execute("SELECT id FROM renters WHERE nama = %s", (nama_renter,))
    renter_id = cursor.fetchone()
    
    if not renter_id:
        return "\nPenyewa tidak ditemukan."

    # Tambahkan penyewaan ke database
    cursor.execute("""
        INSERT INTO rentals (renter_id, plat_nomor, jumlah_hari, tanggal_sewa, tanggal_kembali) 
        VALUES (%s, %s, %s, %s, %s)
    """, (renter_id[0], car_id, rented_day, tanggal_sewa, tanggal_kembali))
    
    # Update last_status dan last_update di tabel cars
    cursor.execute("""
        UPDATE cars SET last_status = %s, last_update = %s WHERE plat_nomor = %s
    """, ("disewa", tanggal_sewa, car_id))
    db.commit()

    return f"\nMobil {car_id} berhasil disewa oleh {nama_renter}, selama {rented_day} hari.\n" \
           f"Waktu sewa: {tanggal_sewa}\n" \
           f"Tanggal harus dikembalikan: {tanggal_kembali}"

def return_car(nama_renter: str) -> str:
    """Mengembalikan mobil yang disewa."""
    db = connect_db()
    cursor = db.cursor()

    # Cek apakah penyewa sedang menyewa mobil
    cursor.execute("""
        SELECT r.plat_nomor FROM rentals r
        JOIN renters re ON r.renter_id = re.id
        WHERE re.nama = %s
    """, (nama_renter,))
    rental = cursor.fetchone()

    if not rental:
        print("Anda tidak meminjam mobil.")
        return

    plat_mobil_disewa = rental[0]
    print(f"Mobil yang Anda pinjam adalah '{plat_mobil_disewa}'")

    car_id = input("Masukkan plat nomor mobil yang ingin dikembalikan: ").upper().strip()

    if car_id != plat_mobil_disewa:
        print(f"Anda hanya dapat mengembalikan mobil yang Anda pinjam: '{plat_mobil_disewa}'")
        return

    # Hapus data penyewaan dari database
    cursor.execute("DELETE FROM rentals WHERE plat_nomor = %s", (car_id,))
    
    # Update last_status dan last_update di tabel cars
    cursor.execute("""
        UPDATE cars SET last_status = %s, last_update = NOW() WHERE plat_nomor = %s
    """, ("tersedia", car_id))
    db.commit()

    print(f"Mobil '{car_id}' berhasil dikembalikan.")
