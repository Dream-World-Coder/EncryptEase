from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64
import os

def encrypt_file(key, input_file_path, output_file_path):
    try:
        # Read the content of the input file
        with open(input_file_path, 'rb') as f:
            file_data = f.read()

        # Generate a random nonce
        nonce = os.urandom(16)  # Standard nonce size for CTR is 16 bytes

        cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), backend=default_backend())
        encryptor = cipher.encryptor()

        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(file_data) + padder.finalize()

        ciphertext = encryptor.update(padded_data) + encryptor.finalize()

        # Encode the nonce and ciphertext together
        encrypted_message = nonce + ciphertext
        encoded_encrypted_message = base64.b64encode(encrypted_message)

        # Write the encoded encrypted content to the output file
        with open(output_file_path, 'wb') as f:
            f.write(encoded_encrypted_message)

        return "File encrypted successfully."
    
    except Exception as e:
        return f'Some error occurred, Please Try again.\n\t{e}'


def encrypt_file_name_also(key, input_file_path):
    try:
        with open(input_file_path, 'rb') as f:
            file_data = f.read()
            
        file_name = os.path.basename(input_file_path)
        name, ext = os.path.splitext(file_name)

        nonce = os.urandom(16)  # Standard nonce size for CTR is 16 bytes

        cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), backend=default_backend())
        encryptor = cipher.encryptor()

        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(file_data) + padder.finalize()
        padded_data2 = padder.update(file_name) + padder.finalize()
        
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        ciphername = encryptor.update(padded_data2) + encryptor.finalize()

        encrypted_message = nonce + ciphertext
        encrypted_file_name = nonce + ciphername
        encoded_encrypted_message = base64.b64encode(encrypted_message)

        with open(encrypted_file_name, 'wb') as f:
            f.write(encoded_encrypted_message)

        return "File encrypted successfully."
    
    except Exception as e:
        return f'Some error occurred, Please Try again.\n\t{e}'



if __name__ == "__main__":
    key = b'\xe0\xa9H\xab8\xfa\x01\xd5\xd7v\xff\x16,r2\x11\x8b\xfd\x8f\x9f_n\xe0Hbeq\x1e{\xd8\x02\x9c'
    input_file_path = input("\n\tEnter the path of the file to encrypt: ")
    # output_file_path = input("\n\tEnter the path to save the encrypted file: ")
    output_file_path = input_file_path
    # result = encrypt_file(key, input_file_path, output_file_path)
    result = encrypt_file_name_also(key=key, input_file_path=input_file_path)
    print(result)
