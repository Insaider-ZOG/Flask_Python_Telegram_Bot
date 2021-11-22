import requests

from telegram_bot_app.models.telegram_models import Account
from telegram_bot_app.models import dbase
from telegram_bot_app.config import TELEGRAM_SEND_MESSAGE_URL


class TelegramBot:

    def __init__(self):
        self.chat_id = None
        self.text = None
        self.first_name = None
        self.last_name = None

    def parse_webhook_data(self, data):
        message = data['message']
        self.chat_id = message['chat']['id']
        self.incoming_message_text = message['text'].lower()
        self.first_name = message['from']['first_name']


    def action(self):
        success = None

        account = Account(
            telegram_id=self.chat_id,
            account_name=self.first_name)

        first_name_in_db = Account.find_by_account_name(account.account_name)

        if self.incoming_message_text == '/start':

            if first_name_in_db:
                self.outgoing_message_text = "Hello, but {} in DBase!".format(self.first_name)
                success = self.send_message()
            else:
                dbase.session.add(account)
                dbase.session.commit()
                self.outgoing_message_text = "Hi, i was addad {} in DBase!".format(self.first_name)
                success = self.send_message()

        if self.incoming_message_text == '/delete':

            if not first_name_in_db:
                self.outgoing_message_text = "{} account not found.".format(self.first_name)
                success = self.send_message()
            else:
                dbase.session.delete(first_name_in_db)
                dbase.session.commit()
                self.outgoing_message_text = "!!HI, I DELETED THR ACCOUNT {} FROM THE DBASE!!".format(self.first_name)
                success = self.send_message()

        if self.incoming_message_text == '/me':
            self.outgoing_message_text = "{} {}".format(self.first_name, self.chat_id)
            success = self.send_message()

        return success


    def send_message(self):
        res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(self.chat_id, self.outgoing_message_text))
        return True if res.status_code == 200 else False