# Configuration


class BaseConfig(object):
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    ENV = "development"
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///extract-py/develop.db"
    SECRET_KEY = "08390129adaea24e1c0a3b5b"


class TestingConfig(BaseConfig):
    ENV = "testing"
    TESTING = True
    SECRET_KEY = "419a4ade33fb40553a294898"
