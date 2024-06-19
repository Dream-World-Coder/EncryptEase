from flask import Flask, render_template, request, send_file
import os
import logging
from user_agents import parse
from python_functions.key_generator import make_random_key

# msg/ Txt ciphers
from python_functions.encryption.mode_ecb import encrypt_message
from python_functions.decryption.mode_ecb import decrypt_message

# File Ciphers
from python_functions.encryption.file_encrypt.mode_ctr import encrypt_file
from python_functions.decryption.file_decrypt.mode_ctr import decrypt_file

import tempfile

app = Flask(__name__)

# Ensuring the log directory exists
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
    return render_template('index.html', max_size=10)

@app.route('/gen_key', methods=['POST'])
def gen_key():
    key_size = int(request.form["gen_key"])
    key = make_random_key(key_size=key_size)
    return {"key": key.hex()}

@app.route('/encrypt', methods=['POST'])
def encrypt():
    message = request.form["message"]
    key_hex = request.form["key"]
    try:
        key = bytes.fromhex(key_hex)  # Convert hex string back to bytes
        encrypted_msg = encrypt_message(key=key, message=message.encode('utf-8'))
        return {"encrypted_msg": encrypted_msg.decode('utf-8'), "key": key_hex}
    except Exception as e:
        return {"error": f"Encryption error: {e}"}

@app.route('/encrypt_file_route', methods=['POST'])
def encrypt_file_route():
    if 'file' not in request.files or 'key' not in request.form:
        return {"error": "File and key are required."}
    
    uploaded_file = request.files['file']
    save_path = os.path.join(tempfile.gettempdir(), uploaded_file.filename)
    output_path = save_path
    uploaded_file.save(save_path)
    
    key_hex = request.form["key"]
    try:
        key = bytes.fromhex(key_hex)
        encrypt_file(key=key, input_file_path=save_path, output_file_path=output_path)
        
        response = send_file(output_path, as_attachment=True, download_name=uploaded_file.filename)
        response.call_on_close(lambda: os.remove(save_path))
        response.call_on_close(lambda: os.remove(output_path))
        return response
    
    except Exception as e:
        return {"error": f"Encryption error: {e}"}

@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_msg = request.form["encrypted_msg"]
    key_hex = request.form["key"]
    try:
        key = bytes.fromhex(key_hex)  # Convert hex string back to bytes
        decrypted_msg = decrypt_message(key=key, ciphertext=encrypted_msg.encode('utf-8'))
        return {"decrypted_msg": decrypted_msg.decode('utf-8'), "key": key_hex}
    except Exception as e:
        return {"error": f"Decryption error: {e}"}

@app.route('/decrypt_file_route', methods=['POST'])
def decrypt_file_route():
    if 'encrypted_file' not in request.files or 'key' not in request.form:
        return {"error": "File and key are required."}
    
    uploaded_file = request.files['encrypted_file']
    save_path = os.path.join(tempfile.gettempdir(), uploaded_file.filename)
    output_path = save_path
    uploaded_file.save(save_path)
    
    key_hex = request.form["key"]
    try:
        key = bytes.fromhex(key_hex)
        decrypt_file(key=key, input_file_path=save_path, output_file_path=output_path)
        
        response = send_file(output_path, as_attachment=True, download_name=uploaded_file.filename)
        response.call_on_close(lambda: os.remove(save_path))
        response.call_on_close(lambda: os.remove(output_path))
        return response
    
    except Exception as e:
        return {"error": f"Decryption error: {e}"}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5500)
