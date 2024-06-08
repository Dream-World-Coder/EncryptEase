
# Secret Message Encryption and Decryption

This project demonstrates a simple message encryption and decryption using the AES encryption algorithm. It includes an encryptor script (`encryptor.py`) for message encryption and a decryptor script (`decryptor.py`) for message decryption.
***
The key size for AES must be 16, 24, or 32 bytes (corresponding to AES-128, AES-192, or AES-256, respectively). If the key size is different, you may encounter errors .
***


## Installation

### Linux and Mac OS

To install Python and the required cryptography module on Linux or Mac OS, run the following command:

./install.sh

### Windows

To install Python and the required cryptography module on Windows, run the following command in Command Prompt:

install.bat




## Usage

### Encryption

Run the encryptor script (`encryptor.py`), enter your message when prompted, and copy the encrypted message.

python encryptor.py [for WINDOWS]
python3 encryptor.py [for MAC]

### Decryption

Run the decryptor script (`decryptor.py`), paste the encrypted message when prompted, and the original message will be displayed.

python decryptor.py [for WINDOWS]
python3 decryptor.py [for MAC]



## Requirements

Ensure you have Python installed. The installation scripts will install the required cryptography module.




## Notes

- Keep your encryption key secure.
- The key size for AES must be 16, 24, or 32 bytes
- Use strong, unique keys for better security.
- This is a basic example and may not cover all security considerations.
