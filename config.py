import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super_secret_key'
    API_KEY = os.environ.get('API_KEY') or 'donotsharewithanyone'
    DEBUG = os.environ.get('DEBUG') or True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:8887@localhost:5432/tinyblog"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PERMANENT_SESSION_LIFETIME = 130

    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_PORT = os.environ.get('MAIL_PORT') or 587
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or 1
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'websitetestwebsitetest@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['websitetestwebsitetest@gmail.com', 'mauran.mango@gmail.com']
