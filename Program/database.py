import mysql.connector

def connect_db():
    """Membuat koneksi ke database MySQL."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Himmel.134",  # Ganti dengan password MySQL kamu
        database="rental_mobil"
    )
