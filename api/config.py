import os

basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
PORT = 5000
HOST = "127.0.0.1"
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(DB_USER="postgres_user", DB_PASS="postgres_password", DB_ADDR="127.0.0.1", DB_NAME="chat_bot")
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

print(SQLALCHEMY_DATABASE_URI)
print(SQLALCHEMY_MIGRATE_REPO)