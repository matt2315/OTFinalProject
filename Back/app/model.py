from flask_sqlalchemy import SQLAlchemy
from config import Configuration

db = SQLAlchemy()

class Account(db.Model):
    __tablename__ = Configuration.USER_TABLENAME
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('accountUsername', db.Text)
    password = db.Column('accountPassword', db.Text)

    def __init__(self, username, password):
        self.username = username
        self.password = password

class ticket(db.Model):
    __tablename__= Configuration.TICKET_TABLENAME
    tId = db.Column('ticketId', db.Integer, primary_key=True)
    mTitle = db.Column('movieTitle', db.Text)
    tDatePurchased = db.Column('ticketDatePurchased', db.Text)
    tPrice = db.Column('ticketPrice', db.Integer)
    tQuantity = db.Column('ticketQuantity', db.Integer)

    def __init__(self, mTitle, tDatePurchased, tPrice, tQuantity):
        self.mTitle = mTitle
        self.tDatePurchased =tDatePurchased
        self.tPrice = tPrice
        self.tQuantity = tQuantity

class histories(db.Model):
    __tablename__=Configuration.HISTORY_TABLENAME
    history_Id = db.Column('historyId', db.Integer, primary_key=True)
    history_Date = db.Column('historyDate', db.Text)
    total_sale = db.Column('totalSale', db.Integer)
    total_ticket_quantity = db.Column('totalticketQuantity', db.Integer)

    def __init__(self, history_Date, total_sale, total_ticket_quantity):
        self.history_Date = history_Date
        self.total_sale = total_sale
        self.total_ticket_quantity = total_ticket_quantity
