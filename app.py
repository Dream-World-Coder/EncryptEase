from flask import Flask, render_template, request
from python_functions.key_generator import make_random_key
from python_functions.encryptor import encrypt_message
from python_functions.decryptor import decrypt_message

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/gen_key', methods=['POST'])
def gen_key():
    key_size = int(request.form["gen_key"])
    key = make_random_key(key_size=key_size)
    return render_template('index.html', key=key.hex())  # Convert key to hex for display

@app.route('/encrypt', methods=['POST'])
def encrypt():
    message = request.form["message"]
    key_hex = request.form["key"]
    try:
        key = bytes.fromhex(key_hex)  # Convert hex string back to bytes
        encrypted_msg = encrypt_message(key=key, message=message.encode('utf-8'))
        return render_template('index.html', encrypted_msg=encrypted_msg.decode('utf-8'), key=key_hex)
    except Exception as e:
        return render_template('index.html', error=f"Encryption error: {e}")

@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_msg = request.form["encrypted_msg"]
    key_hex = request.form["key"]
    try:
        key = bytes.fromhex(key_hex)  # Convert hex string back to bytes
        decrypted_msg = decrypt_message(key=key, ciphertext=encrypted_msg.encode('utf-8'))
        return render_template('index.html', decrypted_msg=decrypted_msg.decode('utf-8'), key=key_hex)
    except Exception as e:
        return render_template('index.html', error=f"Decryption error: {e}")

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5001)

  
  # key not required, add a deault value, and id= generate button, also add doccumnetation
  # msg = {{msg}} show in sepeate div
  # 16 byte
  # b'\xa8\x11`7\x03x\x0fS\x02\x19\xaa\x80#1\xcb\xb3'
  # Invalid key size (392) for AES.
  # b"b'\\xa8\\x11`7\\x03x\\x0fS\\x02\\x19\\xaa\\x80#1\\xcb\\xb3'"
  
#   file encrypting, contact svgs, documentations and sidde theke dichu appear on scroll 
# 



# contacts er niche dan dik e faq box deoa jete pare