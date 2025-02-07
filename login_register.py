renter_acc = {'td' : 'td' # Dictionary untuk menyimpan data mobil. Key = ID, Values = Password
}

def get_user(user: str, pwd: str) -> str:
    """Get user id and password

    Args:
        user (str): id_renter
        pwd (str): pwd_renter

    Returns:
        str: Pesan status
    """
    if user in renter_acc and renter_acc[user] == pwd:
        return "Login berhasil"
    else:
        return "ID atau password salah"
