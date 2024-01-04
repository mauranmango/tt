import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super_secret_key'
    API_KEY = os.environ.get('API_KEY') or 'donotsharewithanyone'
    DEBUG = os.environ.get('DEBUG') or True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:8887@localhost:5432/tinyblog"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PERMANENT_SESSION_LIFETIME = 130
