'''
The key size for AES must be 16, 24, or 32 bytes (corresponding to AES-128, AES-192, or AES-256, respectively). 
If the key size is different, you may encounter errors.
'''
import os

# Generate a random 32-byte key
random_key = os.urandom(32)

print("Random 32-byte key:", random_key)
