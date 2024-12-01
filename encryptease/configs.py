import os

class Config:
    FLASK_APP = os.getenv("FLASK_APP", "run")
    PORT=os.getenv("PORT", 5500)
    SECRET_KEY = os.getenv("SECRET_KEY", os.urandom(128))
    # print(f"\n{PORT=}\n{SECRET_KEY=}\n\n")
    # why printing 2 times? first 5500 then 8000


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
