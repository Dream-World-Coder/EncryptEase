from ...encryptease import app
from flask import render_template, request, jsonify
from cryptography_functions.key_generator import make_random_key
import os
import logging
from user_agents import parse

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


