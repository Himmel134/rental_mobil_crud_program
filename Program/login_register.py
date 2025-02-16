renters_data = {}  # Dictionary untuk menyimpan biodata renter

def login(nama: str, pwd: str) -> str:
    """Memeriksa login berdasarkan nama dan password.

    Args:
        user (str): ID pengguna (renter).
        pwd (str): Password pengguna.

    Returns:
        str: Pesan status login.
    """
    if nama in renters_data:
        if renters_data[nama]["password"] == pwd:  
            return "Login berhasil"
        else:
            return "Password salah!"
    else:
        return "Nama tidak ditemukan!"

def register(nama: str, pwd: str) -> str:
    """Mendaftarkan penyewa baru dengan ID, nama, KTP, dan password.

    Args:
        id_renter (str): ID pengguna yang ingin didaftarkan.
        pwd_renter (str): Password pengguna.

    Returns:
        str: Pesan status pendaftaran.
    """
    if nama in renters_data:
        return "Nama sudah terdaftar. Kembali ke menu utama."

    print("\n=== Pendaftaran Biodata ===")

    ktp_renter = input("Masukkan Nomor KTP (minimal 10 digit): ").strip()
    if not ktp_renter.isnumeric() or len(ktp_renter) < 10 or any(renter['ktp'] == ktp_renter for renter in renters_data.values()):
        return "Nomor KTP tidak valid. Kembali ke menu utama."

    # Simpan ke dictionary
    renters_data[nama] = {
        "ktp": ktp_renter,
        "password": pwd
    }

    return f"Pendaftaran berhasil! Selamat datang, {nama}."
