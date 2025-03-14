-- Hapus database jika sudah ada, lalu buat ulang
DROP DATABASE IF EXISTS rental_mobil;

-- Buat database rental mobil
CREATE DATABASE IF NOT EXISTS rental_mobil;
USE rental_mobil;

-- Buat tabel penyewa (renters)
CREATE TABLE IF NOT EXISTS renters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100) UNIQUE NOT NULL,
    ktp VARCHAR(20) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Buat tabel mobil (cars)
CREATE TABLE IF NOT EXISTS cars (
    plat_nomor VARCHAR(10) PRIMARY KEY,
    merek VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    tahun INT NOT NULL,
    harga_sewa_per_hari INT NOT NULL,
    last_update DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    last_status VARCHAR(20) DEFAULT 'tersedia'
);

-- Buat tabel penyewaan mobil (rentals)
CREATE TABLE IF NOT EXISTS rentals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    renter_id INT NOT NULL,
    plat_nomor VARCHAR(10) NOT NULL,
    jumlah_hari INT NOT NULL,
    tanggal_sewa DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    tanggal_kembali DATETIME NOT NULL,
    FOREIGN KEY (renter_id) REFERENCES renters(id) ON DELETE CASCADE,
    FOREIGN KEY (plat_nomor) REFERENCES cars(plat_nomor) ON DELETE CASCADE
);

-- Masukkan data awal ke tabel mobil
INSERT INTO cars (plat_nomor, merek, model, tahun, harga_sewa_per_hari) VALUES
('AE3221', 'Toyota', 'Avanza', 2020, 300000),
('AE7259', 'Honda', 'Civic', 2021, 500000),
('AE5761', 'Suzuki', 'Ertiga', 2018, 350000),
('AE1782', 'Suzuki', 'Karimun', 2013, 250000);
