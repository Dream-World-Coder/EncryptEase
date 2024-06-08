from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64

def decrypt_message(key, ciphertext):
    try:
        print(f'\n\nDecoding: key={key}, message={ciphertext}')
        cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
        decryptor = cipher.decryptor()

        padded_data = decryptor.update(base64.b64decode(ciphertext)) + decryptor.finalize()

        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        message = unpadder.update(padded_data) + unpadder.finalize()
        return message
    except Exception as e:
        return f'Some error occured, Pls Try again.\n\t{e}'

if __name__ == "__main__":
    key = b'\xe0\xa9H\xab8\xfa\x01\xd5\xd7v\xff\x16,r2\x11\x8b\xfd\x8f\x9f_n\xe0Hbeq\x1e{\xd8\x02\x9c'

    ciphertext = input("\n\tEnter the encrypted message: ")

    decrypted_message = decrypt_message(key, ciphertext)
    print("\tDecrypted Message:", decrypted_message.decode('utf-8'))
    print("")

