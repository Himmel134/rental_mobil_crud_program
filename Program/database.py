import mysql.connector

def connect_db():
    """Membuat koneksi ke database rental_mobil."""
    return mysql.connector.connect(
        host="localhost",
        user="root", 
        password="Himmel.134",
        database="rental_mobil"
    )
