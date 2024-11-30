from flask import  render_template, request
from flask import jsonify
from cryptography_functions.key_generator import make_random_key
from cryptography_functions.encryption.mode_ecb import encrypt_message
from cryptography_functions.decryption.mode_ecb import decrypt_message
from ...encryptease import app


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
