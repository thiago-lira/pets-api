import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.config import config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    env = os.getenv('FLASK_ENV') or 'production'
    app.config.from_object(config[env])

    db.init_app(app)


    from .resources.subscribers import subscribers_bp
    app.register_blueprint(subscribers_bp, url_prefix="/api")

    return app
