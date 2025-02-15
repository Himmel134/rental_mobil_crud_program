renter_acc = {'td' : 'td' # Dictionary untuk menyimpan data mobil. Key = ID, Values = Password
}

def login(user:str, pwd:str) -> str:
    """Get login id and password

    Args:
        user (str): id_renter
        pwd (str): pwd_renter

    Returns:
        str: Pesan status
    """
    if user in renter_acc and renter_acc[user] == pwd:
        return "Login berhasil"
    else:
        return "\nID atau password salah"
    
def register(user: str, pwd: str) -> str:
    """Mendaftar ID dan password

    Args:
        user (str): ID pendaftaran
        pwd (str): Password pendaftaran

    Returns:
        str: Pesan status pendaftaran
    """
    if user in renter_acc:
        return "ID sudah ada"
    else:
        renter_acc[user] = pwd  # Menyimpan ID dan password ke dalam dictionary
        return "\nPendaftaran berhasil"


