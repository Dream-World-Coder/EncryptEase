import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    FLASK_APP = os.getenv("FLASK_APP", "run")
    PORT=os.getenv("PORT", 3000)
    SECRET_KEY = os.getenv("SECRET_KEY", os.urandom(128))


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False


configs_dictionary = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
