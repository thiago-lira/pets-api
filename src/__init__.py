from flask import Flask


def create_app():
    app = Flask(__name__)
    from .resources.subscribers import subscribers_bp
    app.register_blueprint(subscribers_bp, url_prefix="/api")

    return app
