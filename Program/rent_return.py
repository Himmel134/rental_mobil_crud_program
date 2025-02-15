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
    if car_id in status_cars and car_id not in renter_own:
        renter_name = input("Masukkan nama penyewa : ")
        rented_day = input("Masukkan jumlah hari(numerik) : ")
        if rented_day.isnumeric():
            renter_own[id_renter] = {
                'id mobil' : car_id, 
                'penyewa' : renter_name.lower(), 
                'hari' : rented_day.lower(), 
                'merek': status_cars[car_id]['merek']}
            print(renter_own) # -> cek isi dicitionary rented_cars
            return (f"\n{car_id} Berhasil disewa oleh {renter_name}, selama {rented_day} Hari.")
        else:
            return ("Masukkan hari dalam bentuk numerik")
    elif id_renter in renter_own:
        return "\nAnda sudah menyewa mobil lain. Kembalikan dulu sebelum menyewa yang baru."
    elif car_id in [data["id mobil"] for data in renter_own.values()]:
        return "\nMobil sedang disewa oleh orang lain"
    else:
        return("\nMobil tidak ditemukan")
    
def return_car(id_renter:str, car_id:str) -> str:
    """return car

    Args:
        id_renter (str): id_renter
        car_id (str): car_id

    Returns:
        str: renter_own{}
    """
    if car_id in renter_own[id_renter]:
        print(f"ID mobil : {status_cars}, ")
        if id_renter in renter_own and renter_own[id_renter]['id mobil'] == car_id:
            del renter_own[id_renter]
            return(f"{car_id} berhasil dikembalikan")
    else:
        return("Mobil tidak sedang disewa")