from flask import request, send_file
from flask import jsonify
import os
from cryptography_functions.encryption.file_encrypt.mode_ctr import encrypt_file
from cryptography_functions.decryption.file_decrypt.mode_ctr import decrypt_file
import tempfile
from ...encryptease import app


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

