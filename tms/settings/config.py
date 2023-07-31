import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DEBUG = os.environ.get('DEBUG_MODE') == 'True'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    STATIC_FOLDER = os.environ.get('static')
    TEMPLATES_FOLDER = os.environ.get('templates')
