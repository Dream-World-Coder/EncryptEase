from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64

def decrypt_message(key:bytes, ciphertext:str, mode:str="ecb") -> str:
    """
    Decrypts a message using AES-256-ECB mode or AES-256-CTR mode.
    Args:
        key (bytes): The decryption key.
        ciphertext (str): The encrypted message in base64 format.
        mode (str): The mode of decryption ('ecb' or 'ctr').
    Returns:
        str: The decrypted message.
    """
    try:
        mode = mode.lower()
        # Decode the base64 ciphertext
        decoded_ciphertext = base64.b64decode(ciphertext)

        if mode == "ecb":
            cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
            decryptor = cipher.decryptor()

            padded_data = decryptor.update(decoded_ciphertext) + decryptor.finalize()

            unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
            message:bytes = unpadder.update(padded_data) + unpadder.finalize()

        elif mode == "ctr":
            # Extract the nonce (first 16 bytes) from the ciphertext
            nonce = decoded_ciphertext[:16]
            actual_ciphertext = decoded_ciphertext[16:]

            cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), backend=default_backend())
            decryptor = cipher.decryptor()
            
            # CTR mode doesn't need padding
            message:bytes = decryptor.update(actual_ciphertext) + decryptor.finalize()

        else:
            raise ValueError("Mode must be either 'ecb' or 'ctr'")

        return message.decode('utf-8')
    except Exception as e:
        print(f'Error in decryption: {e}')
        raise Exception(f'Error in decryption: {e}')

if __name__ == "__main__":
    key = b'\xe0\xa9H\xab8\xfa\x01\xd5\xd7v\xff\x16,r2\x11\x8b\xfd\x8f\x9f_n\xe0Hbeq\x1e{\xd8\x02\x9c'

    ciphertext = input("\n\tEnter the encrypted message: ")
    mode = input("\tEnter decryption mode (ecb/ctr): ")

    decrypted_message:str = decrypt_message(key, ciphertext, mode)
    print("\tDecrypted Message:", decrypted_message)


