import os


class Production:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')


class Development(Production):
    DEBUG = True


config = {
    'development': Development,
    'production': Production
}
