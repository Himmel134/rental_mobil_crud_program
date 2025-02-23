CREATE DATABASE rental_mobil;

USE rental_mobil;

CREATE TABLE renters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100) UNIQUE,
    ktp VARCHAR(20) UNIQUE,
    password VARCHAR(100)
);

CREATE TABLE cars (
    plat VARCHAR(10) PRIMARY KEY,
    merek VARCHAR(50),
    model VARCHAR(50),
    tahun INT,
    harga_sewa_per_hari INT
);

CREATE TABLE rentals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    renter_nama VARCHAR(100),
    plat_mobil VARCHAR(10),
    hari INT,
    FOREIGN KEY (renter_nama) REFERENCES renters(nama),
    FOREIGN KEY (plat_mobil) REFERENCES cars(plat)
);
