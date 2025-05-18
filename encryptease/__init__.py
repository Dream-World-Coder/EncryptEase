from flask import Flask
from .configs import configs_dictionary




def create_app(configs_dictionary_key="development"):
    app = Flask(__name__)
    app.config.from_object(configs_dictionary[configs_dictionary_key])


    from .components.main.routes import main_bp
    # from .components.logging.routes import log_bp
    from .components.cipher_text.routes import text_bp
    from .components.cipher_file.routes import file_bp


    app.register_blueprint(main_bp)
    # app.register_blueprint(log_bp)
    app.register_blueprint(text_bp)
    app.register_blueprint(file_bp)

    return app
