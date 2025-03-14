from database import connect_db

def login(nama: str, pwd: str) -> str:
    """Memeriksa login berdasarkan nama dan password."""
    db = connect_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT password FROM renters WHERE nama = %s", (nama,))
    result = cursor.fetchone()

    cursor.close()
    db.close()

    if result and result["password"] == pwd:
        return "Login berhasil"
    return "Nama atau password salah!"

def register(nama: str, pwd: str) -> str:
    """Mendaftarkan penyewa baru dengan nama, KTP, dan password."""
    db = connect_db()
    cursor = db.cursor()

    print("\n=== Pendaftaran Biodata ===")

    ktp_renter = input("Masukkan Nomor KTP (minimal 10 digit): ").strip()
    if not ktp_renter.isnumeric() or len(ktp_renter) < 10:
        return "Nomor KTP tidak valid. Kembali ke menu utama."

    try:
        cursor.execute("INSERT INTO renters (nama, ktp, password) VALUES (%s, %s, %s)", (nama, ktp_renter, pwd))
        db.commit()
        message = f"Pendaftaran berhasil! Selamat datang, {nama}."
    except:
        message = "Nama atau KTP sudah terdaftar. Kembali ke menu utama."

    cursor.close()
    db.close()
    return message
