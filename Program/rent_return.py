status_cars = {  # Dicitonary untuk mrnyimpan data mobil
    "AE3221": {
        "merek": "Toyota",
        "model": "Avanza",
        "tahun": 2020,
        "harga_sewa_per_hari": 300_000
    },
    "AE7259": {
        "merek": "Honda",
        "model": "Civic",
        "tahun": 2021,
        "harga_sewa_per_hari": 500_000
    },
    "AE5761": {
        "merek": "Suzuki",
        "model": "Ertiga",
        "tahun": 2018,
        "harga_sewa_per_hari": 350_000
    },
    "AE1782": {
        "merek": "Suzuki",
        "model": "Karimun",
        "tahun": 2013,
        "harga_sewa_per_hari": 250_000
    }
}
renter_own = {}

def rent_car(id_renter:str, car_id:str) -> str:
    """Rent Car

    Args:
        car (str): kondisi mobil

    Returns:
        str: mobil
    """
    # Jika mobil tidak ditemukan di daftar mobil
    if car_id not in status_cars:
        return "\nMobil tidak ditemukan."

    # Jika pengguna sudah menyewa mobil lain, dia tidak bisa menyewa mobil baru
    if id_renter in renter_own:
        return "\nAnda sudah menyewa mobil lain. Kembalikan dulu sebelum menyewa yang baru."

    # Jika mobil sudah disewa oleh penyewa lain
    if any(rent_info['plat mobil'] == car_id for rent_info in renter_own.values()):
        return "\nMobil ini sudah disewa oleh pengguna lain."

    # Input jumlah hari sewa
    rented_day = input("Masukkan jumlah hari(numerik) : ")
    if not rented_day.isnumeric():
        return "\nMasukkan jumlah hari dalam bentuk angka."

    # Jika semua validasi lolos, mobil bisa disewa
    renter_own[id_renter] = {
        'plat mobil': car_id, 
        'hari': rented_day, 
        'merek': status_cars[car_id]['merek']
    }

    return f"\n{car_id} berhasil disewa oleh {id_renter}, selama {rented_day} hari."

    
def return_car(id_renter:str, car_id:str) -> str:
    """return car

    Args:
        id_renter (str): id_renter
        car_id (str): car_id

    Returns:
        str: renter_own{}
    """
    if id_renter in renter_own and renter_own[id_renter]['plat mobil'] == car_id:
        del renter_own[id_renter]
        return f"{car_id} berhasil dikembalikan."
    else:
        return("Mobil tidak sedang disewa")