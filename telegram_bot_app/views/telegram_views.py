from flask import request, jsonify

from telegram_bot_app.views import tele_bp
from .service import TelegramBot


@tele_bp.route('/', methods=["POST"])
def process():

    req = request.get_json()
    bot = TelegramBot()
    bot.parse_webhook_data(req)
    success = bot.action()
    return jsonify(success=success)