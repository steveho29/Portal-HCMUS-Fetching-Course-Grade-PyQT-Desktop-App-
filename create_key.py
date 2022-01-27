import sys
from crypto import generate_key, encrypt

if __name__ == '__main__':
    generate_key()
    token = sys.argv[1] + '%' + sys.argv[2]
    open('credential.key', 'wb+').write(encrypt(token).encode())
