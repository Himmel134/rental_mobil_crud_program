from database import connect_db

def login(nama: str, pwd: str) -> str:
    """Memeriksa login berdasarkan nama dan password dari database."""
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM renters WHERE nama = %s", (nama,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user:
        if user["password"] == pwd:
            return "Login berhasil"
        else:
            return "Password salah!"
    else:
        return "Nama tidak ditemukan!"

def register(nama: str, pwd: str) -> str:
    """Mendaftarkan penyewa baru dengan nama, KTP, dan password ke database."""
    conn = connect_db()
    cursor = conn.cursor()

    # Cek apakah nama sudah terdaftar
    cursor.execute("SELECT COUNT(*) FROM renters WHERE nama = %s", (nama,))
    if cursor.fetchone()[0] > 0:
        cursor.close()
        conn.close()
        return "Nama sudah terdaftar. Kembali ke menu utama."

    print("\n=== Pendaftaran Biodata ===")

    # Memasukkan nomor KTP
    ktp_renter = input("Masukkan Nomor KTP (minimal 10 digit): ").strip()
    cursor.execute("SELECT COUNT(*) FROM renters WHERE ktp = %s", (ktp_renter,))
    
    if not ktp_renter.isnumeric() or len(ktp_renter) < 10 or cursor.fetchone()[0] > 0:
        cursor.close()
        conn.close()
        return "Nomor KTP tidak valid atau sudah terdaftar. Kembali ke menu utama."

    # Simpan ke database
    cursor.execute("INSERT INTO renters (nama, ktp, password) VALUES (%s, %s, %s)", (nama, ktp_renter, pwd))
    conn.commit()

    cursor.close()
    conn.close()

    return f"Pendaftaran berhasil! Selamat datang, {nama}."
