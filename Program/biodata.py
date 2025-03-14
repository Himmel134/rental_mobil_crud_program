from database import connect_db

def biodata_menu():
    """Menampilkan biodata mobil."""
    db = connect_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT plat_nomor, merek, model, last_status, last_update FROM cars")
    cars = cursor.fetchall()

    print("\n=== STATUS MOBIL ===")
    for car in cars:
        print(f"{car['plat_nomor']}: {car['merek']} {car['model']} - Status: {car['last_status']}, Terakhir Diperbarui: {car['last_update']}")
    
    cursor.close()
    db.close()

def ubah_status_mobil():
    """Memungkinkan admin untuk mengubah status mobil."""
    db = connect_db()
    cursor = db.cursor()

    plat_nomor = input("Masukkan plat nomor mobil yang ingin diubah statusnya: ").upper().strip()
    status_baru = input("Masukkan status baru (tersedia/disewa/diperbaiki): ").strip().lower()
    
    if status_baru not in ["tersedia", "disewa", "diperbaiki"]:
        print("Status tidak valid!")
        return

    cursor.execute("""
        UPDATE cars SET last_status = %s, last_update = NOW() WHERE plat_nomor = %s
    """, (status_baru, plat_nomor))
    db.commit()

    print(f"Status mobil {plat_nomor} berhasil diperbarui menjadi '{status_baru}'.")
    
    cursor.close()
    db.close()
