import os

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:admin@localhost:5432/test'
SQLALCHEMY_TRACK_MODIFICATIONS = False
