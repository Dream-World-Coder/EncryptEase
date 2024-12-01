from flask import Blueprint, render_template, jsonify, request
from .._utility__functions.key_generator import make_random_key

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def home():
  return render_template('index.html', max_size=30) # + in cipher_file bp



@main_bp.route('/generate-key', methods=['POST'])
def gen_key():
    try:
        key_size = int(request.form["gen_key"])
    except Exception:
        return jsonify({"error":"some error in key."}), 400

    if key_size not in [16, 24, 32]:
        return jsonify({"error":"wrong key size"}), 400

    key = make_random_key(key_size=key_size)
    return jsonify({"generatedKey": key.hex()}), 200
