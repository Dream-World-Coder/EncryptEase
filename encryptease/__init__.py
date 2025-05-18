from flask import Flask
from .configs import configs_dictionary
from flask_cors import CORS


def create_app(configs_dictionary_key="development"):
    app = Flask(__name__)
    app.config.from_object(configs_dictionary[configs_dictionary_key])


    cors = CORS()
    cors.init_app(app, origins=["http://localhost:5173","http://127.0.0.1:5173","https://splitexx.netlify.app"])


    from .components.main.routes import main_bp
    # from .components.logging.routes import log_bp
    from .components.cipher_text.routes import text_bp
    from .components.cipher_file.routes import file_bp


    app.register_blueprint(main_bp)
    # app.register_blueprint(log_bp)
    app.register_blueprint(text_bp)
    app.register_blueprint(file_bp)

    return app
