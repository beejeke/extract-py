import os

from flask import Flask
from flask_migrate import Migrate

import config
from extract.model import db
from extract.views import frontend


def get_config(config_name=None):
    """
    Get configuration for `config_name`.

    If `config_name` is None defaults to environment variable `FLASK_ENV`.
    If this is not defined, defaults to "development"
    """
    name = (config_name or os.getenv("FLASK_ENV", "default")).lower()
    return {
        "development": config.DevelopmentConfig,
        "testing": config.TestingConfig,
        "default": config.DevelopmentConfig,
    }[name]()


def create_app(config_name=None):
    """
    Create a Flask application.
    """
    app = Flask(__name__)
    app.config.from_object(get_config(config_name))
    db.init_app(app)
    Migrate(app, db)
    db.create_all(app=app)
    app.register_blueprint(frontend)
    return app