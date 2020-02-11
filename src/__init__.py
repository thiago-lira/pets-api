import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from src.config import config


db = SQLAlchemy()
cors = CORS()


def create_app():
    app = Flask(__name__)
    env = os.getenv('FLASK_ENV') or 'production'
    app.config.from_object(config[env])

    db.init_app(app)
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})

    from .resources.subscribers import subscribers_bp
    app.register_blueprint(subscribers_bp, url_prefix="/api")

    return app
