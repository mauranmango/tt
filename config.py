import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super_secret_key'
    API_KEY = os.environ.get('API_KEY') or 'donotsharewithanyone'
    DEBUG = os.environ.get('DEBUG') or True
