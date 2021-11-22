from flask.blueprints import Blueprint


tele_bp = Blueprint('tele', __name__)

from . import telegram_views