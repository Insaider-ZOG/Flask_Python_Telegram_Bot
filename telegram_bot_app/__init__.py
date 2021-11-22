from flask import Flask
from flask_migrate import Migrate
from telegram_bot_app.config import DevelopmentConfig
from telegram_bot_app.views import tele_bp
from telegram_bot_app.models import dbase


migrate = Migrate()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(DevelopmentConfig)

    dbase.init_app(app)
    migrate.init_app(app, dbase)

    app.register_blueprint(tele_bp)

    return app