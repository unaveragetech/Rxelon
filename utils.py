from cryptography.fernet import Fernet

def encrypt(data, key):
    f = Fernet(key)
    return f.encrypt(data.encode())

def decrypt(data, key):
    f = Fernet(key)
    return f.decrypt(data).decode()
