from telegram_bot_app.models import dbase


class Account(dbase.Model):
    __tablename__ = 'accounts'
    id = dbase.Column(dbase.Integer, primary_key=True)
    telegram_id = dbase.Column(dbase.String(50))
    account_name = dbase.Column(dbase.String(50))

    def __init__(self, telegram_id, account_name):
        self.telegram_id = telegram_id
        self.account_name = account_name

    def __repr__(self):
        return f"<Account : {self.account_name}>"

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_telegram_id(cls, telegram_id):
        return cls.query.filter_by(telegram_id=telegram_id).first()

    @classmethod
    def find_by_account_name(cls, account_name):
        return cls.query.filter_by(account_name=account_name).first()