from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64

def encrypt_message(key, message):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(message) + padder.finalize()

    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return base64.b64encode(ciphertext)

if __name__ == "__main__":
    key = b'\x15\xfa\xe3?\x17{<\x8b\xf9\x1b\xff"_j\x1f_\xbc\xc0\x88\x86lj\xbc \x8a\xb2&s<\xd1\x88A'
    
    message = input("\n\tEnter the message to encrypt: ").encode('utf-8')
    
    encrypted_message = encrypt_message(key, message)
    print("\tEncrypted Message:\n",encrypted_message.decode('utf-8'))

