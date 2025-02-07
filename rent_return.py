from login_register import renter_acc

status_cars = {  # Dicitonary untuk mrnyimpan data mobil
    "mobil 1": {
        "merek": "Toyota",
        "model": "Avanza",
        "tahun": 2020,
        "harga_sewa_per_hari": 300_000
    },
    "mobil 2": {
        "merek": "Honda",
        "model": "Civic",
        "tahun": 2021,
        "harga_sewa_per_hari": 500_000
    },
    "mobil 3": {
        "merek": "Suzuki",
        "model": "Ertiga",
        "tahun": 2019,
        "harga_sewa_per_hari": 350_000
    }
}
rented_cars = {}  # Dictionary untuk menyimpan data mobil yang sedang disewa
renter_own = {}

def rent_car(car_id:str) -> str:
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
            renter_own[car_id] = {'penyewa' : renter_name.lower(), 'hari' : rented_day.lower(), 'merek': status_cars[car_id]['merek']}
            # print(renter_own) # -> cek isi dicitionary rented_cars
            return (f"\n{car_id} Berhasil disewa oleh {renter_name}, {rented_day} Hari.")
        else:
            return ("Masukkan hari dalam bentuk numerik")
    elif car_id in rented_cars:
        return("\nMobil sedang disewa oleh orang lain")
    else:
        return("\nMobil tidak ditemukan")
    
def return_car(car_id:str) -> str:
    """return car

    Args:
        car_id (str): id mobil

    Returns:
        str: car_id
    """
    if car_id in rented_cars:
        print(f"ID mobil : {status_cars}, ")
        del rented_cars[car_id]
        return(f"{car_id} berhasil dikembalikan")
    elif car_id not in rented_cars:
        return("Mobil tidak sedang disewa")
    
