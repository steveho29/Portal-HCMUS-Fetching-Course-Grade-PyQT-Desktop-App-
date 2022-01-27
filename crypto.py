"""
    @Author: Minh Duc
    @Since: 1/27/2022 2:07 PM
"""

from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    return open("secret.key", "rb").read()


def encrypt(s):
    key = load_key()
    b_str = s.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(b_str)
    return encrypted_message.decode()


def decrypt(s):
    b_str = s.encode()
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(b_str)
    return decrypted_message.decode()
