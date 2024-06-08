from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64

def decrypt_message(key, ciphertext):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()

    padded_data = decryptor.update(base64.b64decode(ciphertext)) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    message = unpadder.update(padded_data) + unpadder.finalize()
    return message

if __name__ == "__main__":
    key = b'\x15\xfa\xe3?\x17{<\x8b\xf9\x1b\xff"_j\x1f_\xbc\xc0\x88\x86lj\xbc \x8a\xb2&s<\xd1\x88A'

    ciphertext = input("\n\tEnter the encrypted message: ")

    decrypted_message = decrypt_message(key, ciphertext)
    print("\tDecrypted Message:", decrypted_message.decode('utf-8'))
    print("")

