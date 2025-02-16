# ================================
# Proses Penyewaan & Pengembalian
# ================================

status_cars = {  # Dictionary untuk menyimpan data mobil
    "AE3221": {"merek": "Toyota", "model": "Avanza", "tahun": 2020, "harga_sewa_per_hari": 300_000},
    "AE7259": {"merek": "Honda", "model": "Civic", "tahun": 2021, "harga_sewa_per_hari": 500_000},
    "AE5761": {"merek": "Suzuki", "model": "Ertiga", "tahun": 2018, "harga_sewa_per_hari": 350_000},
    "AE1782": {"merek": "Suzuki", "model": "Karimun", "tahun": 2013, "harga_sewa_per_hari": 250_000}
}

renter_own = {}

def rent_car(nama_renter: str, car_id: str) -> str:
    """Menyewa mobil berdasarkan plat nomor."""

    if car_id not in status_cars:
        return "\nMobil tidak ditemukan."

    if nama_renter in renter_own:
        return "\nAnda sudah menyewa mobil lain. Kembalikan dulu sebelum menyewa yang baru."

    if any(rent_info['plat mobil'] == car_id for rent_info in renter_own.values()):
        return "\nMobil ini sudah disewa oleh pengguna lain."

    rented_day = input("Masukkan jumlah hari (angka): ").strip()

    if not rented_day.isdigit():
        return "\nMasukkan jumlah hari dalam bentuk angka."

    rented_day = int(rented_day)

    renter_own[nama_renter] = {
        'plat mobil': car_id, 
        'hari': rented_day, 
        'merek': status_cars[car_id]['merek']
    }

    return f"\n{car_id} berhasil disewa oleh {nama_renter}, selama {rented_day} hari."


def return_car(nama_renter: str, car_id: str) -> str:
    """Mengembalikan mobil yang disewa."""

    if nama_renter in renter_own and renter_own[nama_renter]['plat mobil'] == car_id:
        del renter_own[nama_renter]
        return f"{car_id} berhasil dikembalikan."
    else:
        return "\nMobil tidak sedang disewa."
