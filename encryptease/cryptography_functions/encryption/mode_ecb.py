from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64

def encrypt_message(key, message):
    try:
        # print(f'\n\nEncoding: key={key}, message={message}')
        cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
        encryptor = cipher.encryptor()

        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(message) + padder.finalize()

        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        return base64.b64encode(ciphertext)
    
    except Exception as e:
        return f'Some error occured, Pls Try again.\n\t{e}'

if __name__ == "__main__":
    key = b'\xe0\xa9H\xab8\xfa\x01\xd5\xd7v\xff\x16,r2\x11\x8b\xfd\x8f\x9f_n\xe0Hbeq\x1e{\xd8\x02\x9c'
    message = input("\n\tEnter the message to encrypt: ").encode('utf-8')    
    encrypted_message = encrypt_message(key, message)
    print("\tEncrypted Message:\n",encrypted_message.decode('utf-8'))

