'''
The key size for AES must be 16, 24, or 32 bytes (corresponding to AES-128, AES-192, or AES-256, respectively). 
If the key size is different, you may encounter errors.
'''
import os

def make_random_key(key_size):
  try:
    random_key = os.urandom(key_size)
    # print("Random 32-byte key:", random_key)
    return random_key
  except Exception as e:
    return f'Some error occured, Pls Try again.\n\t{e}'

print(os.urandom(16).hex())