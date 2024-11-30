from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64

def decrypt_message(key, ciphertext):
    try:
        # Decode the base64 encoded data
        encrypted_data = base64.b64decode(ciphertext)
        
        # Extract the nonce and the ciphertext
        nonce = encrypted_data[:16]  # The first 16 bytes are the nonce
        ciphertext = encrypted_data[16:]

        cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), backend=default_backend())
        decryptor = cipher.decryptor()

        padded_data = decryptor.update(ciphertext) + decryptor.finalize()

        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        decrypted_data = unpadder.update(padded_data) + unpadder.finalize()

        return decrypted_data.decode('utf-8')

    except Exception as e:
        return f'Some error occurred, Please Try again.\n\t{e}'

if __name__ == "__main__":
    key = b'\xe0\xa9H\xab8\xfa\x01\xd5\xd7v\xff\x16,r2\x11\x8b\xfd\x8f\x9f_n\xe0Hbeq\x1e{\xd8\x02\x9c'
    encrypted_message = input("\n\tEnter the encrypted message: ")
    decrypted_message = decrypt_message(key, encrypted_message)
    print("\tDecrypted Message:\n", decrypted_message)
