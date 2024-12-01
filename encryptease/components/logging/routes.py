import os
import logging
from user_agents import parse
from flask import request, Blueprint, current_app


log_bp = Blueprint('log_bp', __name__)


# Ensuring the log directory exists
def initial_logging_setup(log_dir="logs"):
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

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
    current_app.logger.info(log_message)


@log_bp.before_request
def before_request():
    log_request_info()
