import os

from telegram_bot_app import create_app
from telegram_bot_app.models import dbase
from telegram_bot_app.config import DB_NAME



if __name__ == ('__main__'):
    if not os.path.exists(DB_NAME):
        dbase.create_all(app=create_app())
    manager = create_app()
    manager.run()
