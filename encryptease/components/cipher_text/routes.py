from flask import Blueprint, request, jsonify
from .._utility__functions.encryption.encryptor import encrypt_message
from .._utility__functions.decryption.decryptor import decrypt_message
import base64

text_bp = Blueprint('text_bp', __name__)



@text_bp.route('/encrypt/string', methods=['POST'])
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

  maxlen:int = 1.5*1024*1024 # 1.5MB
  if len(message) > maxlen:
    return jsonify({"error": f"message is too long. max {maxlen//1024//1024} MB."}), 400

  try:
    encrypted_msg:str = encrypt_message(key=key_byte, msg=message, mode="ctr") # so the message is in string format
    return jsonify({"encrypted_msg": encrypted_msg, "key": key_hex}), 200 
  except Exception as e:
    return jsonify({"error": f"Encryption error: {e}"}), 500



@text_bp.route('/decrypt/string', methods=['POST'])
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

    maxlen:int = 1.5*1024*1024 # 1.5MB
    if len(encrypted_msg) > maxlen:
        return jsonify({"error": f"encrypted message is too long. max {maxlen//1024//1024} MB."}), 400
    
    # check the encrypted message is base64 encoded
    try:
        base64.b64decode(encrypted_msg)
    except Exception as e:
        return jsonify({"error": f"Invalid encrypted message."}), 400

    try:
        decrypted_msg:str = decrypt_message(key=key_byte, ciphertext=encrypted_msg, mode="ctr")
        return jsonify({"decrypted_msg": decrypted_msg, "key": key_hex}), 200

    except Exception as e:
        return jsonify({"error": f"Decryption error: {str(e)}"}), 500
