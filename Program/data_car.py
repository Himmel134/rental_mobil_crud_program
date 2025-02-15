def data_car(status_cars, renter_own, id_renter, rent_car):
    while True:
        print("\n1. Data seluruh mobil")               
        print("2. Cari mobil berdasarkan plat nomor")
        print("3. Cari mobil berdasarkan merek")
        print("4. Kembali ke menu utama")
        
        check_mobil = input("\nTentukan pilihan Anda: ")

        if check_mobil == '1':
            for plat, info in status_cars.items():    
                status = "Disewa" if id_renter in renter_own and renter_own[id_renter]['id mobil'] == plat else "Tersedia"
                print(f"{plat}: {info['merek']} {info['model']} ({info['tahun']}), Harga Sewa: {info['harga_sewa_per_hari']} Rupiah. Status: {status}")
            
            while True:  # Looping untuk validasi input
                rent_input = input("\nApakah Anda ingin menyewa mobil? (Y/N): ").upper()
                if rent_input == 'Y':
                    car_info = input("\nMasukkan plat nomor mobil yang ingin disewa: ").upper()
                    print(rent_car(id_renter, car_info))
                    break  # Keluar dari loop jika input benar
                elif rent_input == 'N':
                    break  # Keluar dari loop jika memilih tidak menyewa
                else:
                    print("Input tidak valid! Harap masukkan 'Y' atau 'N'.")

        elif check_mobil == '2':
            check_plat = input("\nMasukkan nomor plat mobil yang ingin dicari: ").upper()
            if check_plat in status_cars:
                info = status_cars[check_plat]
                status = "Disewa" if id_renter in renter_own and renter_own[id_renter]['id mobil'] == check_plat else "Tersedia"
                print(f"\n{check_plat}: {info['merek']} {info['model']} ({info['tahun']}), Harga Sewa: {info['harga_sewa_per_hari']} Rupiah. Status: {status}")

                while True:  # Looping untuk validasi input
                    rent_input = input("\nApakah Anda ingin menyewa mobil? (Y/N): ").upper()
                    if rent_input == 'Y':
                        car_info = input("\nMasukkan plat nomor mobil yang ingin disewa: ").upper()
                        print(rent_car(id_renter, car_info))
                        break
                    elif rent_input == 'N':
                        break
                    else:
                        print("Input tidak valid! Harap masukkan 'Y' atau 'N'.")

            else:
                print("Mobil yang Anda cari tidak ada.")

        elif check_mobil == '3':
            check_merek = input("\nMasukkan merek mobil yang ingin dicari: ").capitalize()
            found = False

            for plat, info in status_cars.items():
                if info["merek"] == check_merek:
                    print(f"\n{info['merek']} {info['model']} ({info['tahun']}), Harga Sewa: {info['harga_sewa_per_hari']} Rupiah.")
                    found = True

            if found:
                while True:  # Looping untuk validasi input
                    rent_input = input("\nApakah Anda ingin menyewa mobil? (Y/N): ").upper()
                    if rent_input == 'Y':
                        car_info = input("\nMasukkan plat nomor mobil yang ingin disewa: ").upper()
                        print(rent_car(id_renter, car_info))
                        break
                    elif rent_input == 'N':
                        break
                    else:
                        print("Input tidak valid! Harap masukkan 'Y' atau 'N'.")
            else:
                print("Mobil yang Anda cari tidak ada.")

        elif check_mobil == '4':
            break  # Kembali ke menu utama

        else:
            print("Pilihan tidak valid, silakan coba lagi.")
