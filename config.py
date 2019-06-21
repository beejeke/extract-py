# Configuration

import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "185402ba04e44f53a0845a67c014b411"


class DevelopmentConfig(BaseConfig):
    ENV = "development"
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{ROOT_DIR}/develop.db"
    SECRET_KEY = "08390129adaea24e1c0a3b5b"


class TestingConfig(BaseConfig):
    ENV = "testing"
    TESTING = True
    SECRET_KEY = "419a4ade33fb40553a294898"
