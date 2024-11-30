from flask import Flask, render_template, request, send_file
from flask import jsonify
import os
import logging
from user_agents import parse
from python_functions.key_generator import make_random_key
# import binascii

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
  return render_template('index.html', max_size=17)



@app.route('/generate-key', methods=['POST'])
def gen_key():
  key_size = int(request.form["gen_key"])
  if key_size not in [16, 24, 32]:
    return jsonify({"error":"wrong key size"}), 400

  key = make_random_key(key_size=key_size)
  return jsonify({"generatedKey": key.hex()}), 200



@app.route('/encrypt/string', methods=['POST'])
def encrypt():
  message = request.form["message"]
  key_hex = request.form["key"]

  if not message or not key_hex:
    return jsonify({"error": "message or key is missing."}), 400

  try:
    key_byte = bytes.fromhex(key_hex)  # Converting hex string to bytes
  except ValueError:
    return jsonify({"error": "Invalid key format. Key must be a valid hexadecimal string."}), 400

  if len(key_byte) not in [16, 24, 32]:  # AES requires 16-24-32
    return jsonify({"error": "Invalid key length. Key must be 16, 24, or 32 bytes long."}), 400

  if len(message) > 100000:
    return jsonify({"error": "message is too long. max 100000 characters."}), 400

  try:
    encrypted_msg = encrypt_message(key=key_byte, message=message.encode('utf-8'))
    return jsonify({"encrypted_msg": encrypted_msg.decode('utf-8'), "key": key_hex}), 200
  except Exception as e:
    return jsonify({"error": f"Encryption error: {e}"}), 500


@app.route('/encrypt/file', methods=['POST'])
def encrypt_file_route():
    max_file_size_mb = 17

    # Check for file and key in request
    if 'file' not in request.files or 'key' not in request.form:
        return jsonify({"error": "File and key are required."}), 400

    uploaded_file = request.files['file']
    key_hex = request.form["key"]

    # Save uploaded file temporarily
    save_path = os.path.join(tempfile.gettempdir(), uploaded_file.filename)
    uploaded_file.save(save_path)

    # Check file size limit
    if os.path.getsize(save_path) > max_file_size_mb * 1024 * 1024:
        os.remove(save_path)  # Cleanup the uploaded file
        return jsonify({"error": f"File size is greater than {max_file_size_mb} MB."}), 400

    # Convert and validate the key
    try:
        key_byte = bytes.fromhex(key_hex)
    except ValueError:
        os.remove(save_path)  # Cleanup before returning
        return jsonify({"error": "Invalid key format. Key must be a valid hexadecimal string."}), 400

    if len(key_byte) not in [16, 24, 32]:
        os.remove(save_path)  # Cleanup before returning
        return jsonify({"error": "Invalid key length. Key must be 16, 24, or 32 bytes long."}), 400

    # Define output path for the encrypted file
    output_path = os.path.join(tempfile.gettempdir(), f"encrypted_{uploaded_file.filename}")

    try:
        encrypt_file(key=key_byte, input_file_path=save_path, output_file_path=output_path)

        # Prepare the response with the encrypted file
        response = send_file(output_path, as_attachment=True, download_name=f"encrypted_{uploaded_file.filename}")

        # Clean up files after the response is sent
        response.call_on_close(lambda: os.remove(save_path))
        response.call_on_close(lambda: os.remove(output_path))

        return response, 200

    except Exception as e:
        os.remove(save_path)  # Cleanup on error
        if os.path.exists(output_path):
            os.remove(output_path)
        return jsonify({"error": f"Encryption error: {str(e)}"}), 500




@app.route('/decrypt/string', methods=['POST'])
def decrypt_string_route():
    if 'encrypted_msg' not in request.form or 'key' not in request.form:
        return jsonify({"error": "Encrypted message and key are required."}), 400

    encrypted_msg = request.form["encrypted_msg"]
    key_hex = request.form["key"]

    try:
        key_byte = bytes.fromhex(key_hex)
    except ValueError:
        return jsonify({"error": "Invalid key format. Key must be a valid hexadecimal string."}), 400

    if len(key_byte) not in [16, 24, 32]:
        return jsonify({"error": "Invalid key length. Key must be 16, 24, or 32 bytes long."}), 400

    try:
        decrypted_msg = decrypt_message(key=key_byte, ciphertext=encrypted_msg.encode('utf-8'))
        return jsonify({"decrypted_msg": decrypted_msg.decode('utf-8'), "key": key_hex}), 200

    except Exception as e:
        return jsonify({"error": f"Decryption error: {str(e)}"}), 500



@app.route('/decrypt/file', methods=['POST'])
def decrypt_file_route():
    # Check for file and key in the request
    if 'encrypted_file' not in request.files or 'key' not in request.form:
        return jsonify({"error": "File and key are required."}), 400

    # Save the uploaded file temporarily
    uploaded_file = request.files['encrypted_file']
    save_path = os.path.join(tempfile.gettempdir(), uploaded_file.filename)
    uploaded_file.save(save_path)

    # Convert and validate the key
    key_hex = request.form["key"]
    try:
        key = bytes.fromhex(key_hex)
    except ValueError:
        os.remove(save_path)  # Cleanup the file if key format is invalid
        return jsonify({"error": "Invalid key format. Key must be a valid hexadecimal string."}), 400

    if len(key) not in [16, 24, 32]:
        os.remove(save_path)  # Cleanup before returning
        return jsonify({"error": "Invalid key length. Key must be 16, 24, or 32 bytes long."}), 400

    # Define output path for the decrypted file
    output_path = os.path.join(tempfile.gettempdir(), f"decrypted_{uploaded_file.filename}")

    try:
        decrypt_file(key=key, input_file_path=save_path, output_file_path=output_path)

        # Prepare the response with the decrypted file
        response = send_file(output_path, as_attachment=True, download_name=f"decrypted_{uploaded_file.filename}")

        # Clean up files after the response is sent
        response.call_on_close(lambda: os.remove(save_path))
        response.call_on_close(lambda: os.remove(output_path))

        return response, 200

    except Exception as e:
        os.remove(save_path)  # Cleanup nerror
        if os.path.exists(output_path):
            os.remove(output_path)
        return jsonify({"error": f"Decryption error: {str(e)}"}), 500




if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)
