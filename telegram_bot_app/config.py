import os
from dotenv import load_dotenv

load_dotenv()
DB_NAME = "account"


class Config(object):
    SECRET_KEY = os.urandom(13)
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:12345@localhost/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}



BASE_TELEGRAM_URL = 'https://api.telegram.org/bot{}'.format(os.getenv("TOKEN"))
TELEGRAM_SEND_MESSAGE_URL = BASE_TELEGRAM_URL + '/sendMessage?chat_id={}&text={}'