from flask_sqlalchemy import SQLAlchemy
from config import Configuration

db = SQLAlchemy()

class Account(db.Model):
    __tablename__ = Configuration.USER_TABLENAME
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('accountUsername', db.Unicode)
    password = db.Column('accountPassword', db.Unicode)

    def __init__(self, username, password):
        self.username = username
        self.password = password

class ticket(db.Model):
    __tablename__= Configuration.TICKET_TABLENAME
    tId = db.Column('ticketId', db.Integer, primary_key=True)
    mTitle = db.Column('movieTitle', db.Unicode)
    tDatePurchased = db.Column('ticketDatePurchased', db.Unicode)
    tPrice = db.Column('ticketPrice', db.Integer)
    tQuantity = db.Column('ticketQuantity', db.Integer)

    def __init__(self, mTitle, tDatePurchased, tPrice, tQuantity):
        self.mTitle = mTitle
        self.tDatePurchased =tDatePurchased
        self.tPrice = tPrice
        self.tQuantity = tQuantity
