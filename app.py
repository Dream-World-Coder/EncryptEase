from flask import Flask, render_template, request, g
import os
import logging
from user_agents import parse
from python_functions.key_generator import make_random_key
from python_functions.encryptor import encrypt_message
from python_functions.decryptor import decrypt_message

app = Flask(__name__)

# Ensure the log directory exists
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Configure logging
logging.basicConfig(
    filename=os.path.join(log_dir, 'access.log'),
    level=logging.INFO,
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def log_request_info():
    user_agent = parse(request.headers.get('User-Agent'))
    log_data = {
        "ip": request.remote_addr,
        "method": request.method,
        "path": request.path,
        "device": user_agent.device.family,
        "browser": user_agent.browser.family,
        "browser_version": user_agent.browser.version_string,
        "os": user_agent.os.family,
        "os_version": user_agent.os.version_string
    }
    log_message = (
        f"IP: {log_data['ip']}, "
        f"Method: {log_data['method']}, "
        f"Path: {log_data['path']}, "
        f"Device: {log_data['device']}, "
        f"Browser: {log_data['browser']} {log_data['browser_version']}, "
        f"OS: {log_data['os']} {log_data['os_version']}"
    )
    app.logger.info(log_message)

@app.before_request
def before_request():
    log_request_info()


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