from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64
import os

def encrypt_message(key:bytes, msg:str, mode:str="ecb") -> str:
    """
    Encrypts a message using AES-256-ECB mode or AES-256-CTR mode.
    Args:
        key (bytes): The encryption key.
        msg (str): The message to encrypt.
        mode (str): The mode of encryption ('ecb' or 'ctr').
    Returns:
        str: The encrypted message in base64 format.
    """
    try:
        message:bytes = msg.encode('utf-8')
        mode = mode.lower()

        if mode == "ecb":
            cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
            encryptor = cipher.encryptor()

            padder = padding.PKCS7(algorithms.AES.block_size).padder()
            padded_data = padder.update(message) + padder.finalize()

            ciphertext:bytes = encryptor.update(padded_data) + encryptor.finalize()
            
        elif mode == "ctr":
            # Generate a random 16-byte nonce for CTR mode
            nonce = os.urandom(16)
            cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), backend=default_backend())
            encryptor = cipher.encryptor()
            
            # In CTR mode, we don't need padding since it's a stream cipher
            ciphertext:bytes = encryptor.update(message) + encryptor.finalize()
            # Prepend nonce to ciphertext so it can be used for decryption
            ciphertext = nonce + ciphertext
            
        else:
            raise ValueError("Mode must be either 'ecb' or 'ctr'")

        encoded_ciphertext:bytes = base64.b64encode(ciphertext) # encoded text in bytes
        # now return in string format
        return encoded_ciphertext.decode('utf-8')
    
    except Exception as e:
        print(f'Error in encryption: {e}')
        raise Exception(f'Error in encryption: {e}')

if __name__ == "__main__":
    key:bytes = b'\xe0\xa9H\xab8\xfa\x01\xd5\xd7v\xff\x16,r2\x11\x8b\xfd\x8f\x9f_n\xe0Hbeq\x1e{\xd8\x02\x9c'
    message:str = input("\n\tEnter the message to encrypt: ")
    mode:str = input("\tEnter encryption mode (ecb/ctr): ")
    encrypted_message:str = encrypt_message(key, message, mode)
    print("\tEncrypted Message (base64 string):\n",encrypted_message)

