from flask import Flask, request, jsonify, url_for
from model import *
import datetime
import mysql.connector
from mysql.connector import Error
import click
from flask.cli import FlaskGroup

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Configuration.SQLALCHEMY_DATABASE_URI
db.init_app(app)

@app.route('/logIn',methods = ["GET"])
def userLogin ():
    inputtedUsername = request.args.get('username',0)
    inputtedPassword = request.args.get('password',0)
    checker = Account.query.filter(Account.username == inputtedUsername).first()
    if checker:
        if (checker.password == inputtedPassword):
            return "Logged In"

        else:
            return "wrong password"
    else:
        return "no registered account"

@app.route('/signUp',methods =["POST"])
def userSignup ():
    payload = request.get_json()
    user = payload.get('username', None)
    passw = payload.get('password', None)
    checker = Account.query.filter(Account.username == user).first()
    if checker:
        return "Username already taken"
    else:
        newUser = Account (username = user, password = passw)
        db.session.add(newUser)
        db.session.commit()
        return "signup success"

@app.route('/purchaseTix', methods = ["POST"])
def purchaseSilip():
    payload = request.get_json()
    sQuantity = int (payload.get('silipQuantity', None))
    checker = ticket.query.filter(ticket.mTitle == 'Silip').first()
    if checker:
        checker.tQuantity = checker.tQuantity + sQuantity
        checker.tPrice = checker.tQuantity * 50
        checker.tDatePurchased= datetime.datetime.now().date()
        db.session.commit()
    else:
        newTix = ticket(mTitle = 'Silip', tQuantity = sQuantity, tPrice = sQuantity * 50, tDatePurchased = datetime.datetime.now().date())
        db.session.add(newTix)
        db.session.commit()
    return "Silip ticket reserved"

@app.route('/purchaseTix2', methods = ["POST"])
def purchaseTuyongLumpia():
    payload = request.get_json()
    lQuantity = int (payload.get('TuyongLumpiaQuantity', None))
    checker = ticket.query.filter(ticket.mTitle == 'Tuyong Lumpia').first()
    if checker:
        checker.tQuantity = checker.tQuantity + lQuantity
        checker.tPrice = checker.tQuantity * 50
        checker.tDatePurchased= datetime.datetime.now().date()
        db.session.commit()
    else:
        newTix = ticket(mTitle = 'Tuyong Lumpia', tQuantity = lQuantity, tPrice = lQuantity * 50, tDatePurchased = datetime.datetime.now().date())
        db.session.add(newTix)
        db.session.commit()
    return "Silip ticket reserved"

@app.route('/purchaseTix3', methods = ["POST"])
def purchaseGinataangMani():
    payload = request.get_json()
    gQuantity = int (payload.get('GinataangManiQuantity', None))
    checker = ticket.query.filter(ticket.mTitle == 'Ginataang Mani').first()
    if checker:
        checker.tQuantity = checker.tQuantity + gQuantity
        checker.tPrice = checker.tQuantity * 50
        checker.tDatePurchased= datetime.datetime.now().date()
        db.session.commit()
    else:
        newTix = ticket(mTitle = 'Ginataang Mani', tQuantity = gQuantity, tPrice = gQuantity*50, tDatePurchased = datetime.datetime.now().date())
        db.session.add(newTix)
        db.session.commit()
    return "Silip ticket reserved"



@app.route('/cart',methods=["GET"])
def cart():
    list_tickets = {}
    ticketer = {}
    tickets = ticket.query.filter().all()
    for t in tickets:
        ticketer = {
            'ticket_id': t.tId,
            'movie_title': t.mTitle,
            'ticket_quantity': t.tQuantity,
            'ticket_price': t.tPrice,
            'ticket_date_purchased': t.tDatePurchased
        }
        list_tickets[t.tId]=ticketer
    return jsonify(list_tickets)

@app.route('/update_qty', methods=['GET'])
def up_qty():
    e_id = request.args.get('id', 0)
    movie = ticket.query.filter(ticket.tId == e_id).first()
    return jsonify({'title': movie.mTitle, 'qty':movie.tQuantity})

@app.route('/update_Ticket', methods=['GET'])
def updateTicketing():
    updateQuantity = request.args.get('u_qty', 0)
    updateQuantityMtitle = request.args.get('u_title', 0)
    newQty = ticket.query.filter(ticket.mTitle == updateQuantityMtitle).first()
    newQty.tQuantity = int(updateQuantity)
    db.session.commit()
    return str(updateQuantity)

@app.route('/delete_ticket', methods=["GET"])
def deleteTicketing():
    deleteMtitle = request.args.get('u_title', 0)
    deleteTix = ticket.query.filter(ticket.mTitle == deleteMtitle).first()
    db.session.delete(deleteTix)
    db.session.commit()
    return str("deleted")

@app.route('/purchaseNow',methods=["GET"])
def purchase_now():
    totalPrice = 0
    totalTickets = 0
    addPrice = ticket.query.filter().all()
    for ticketssss in addPrice:
        totalPrice+=ticketssss.tPrice
        totalTickets+=ticketssss.tQuantity
    return str(totalPrice)

@app.route('/toHistory', methods=["POST"])
def to_History():
    totalPrice = 0
    totalTickets = 0
    addPrice = ticket.query.filter().all()
    for ticketssss in addPrice:
        totalPrice+=ticketssss.tPrice
        totalTickets+=ticketssss.tQuantity
    historyTotalPrice = totalPrice
    historyTotalTickets = totalTickets
    newHistory = histories(total_sale = historyTotalPrice, total_ticket_quantity = historyTotalTickets, history_Date = datetime.datetime.now().date())
    db.session.add(newHistory)
    db.session.commit()
    for ticketssss in addPrice:
        db.session.delete(ticketssss)
        db.session.commit()
    return "History made"

@app.route('/gethistory', methods=['GET'])
def gethistory():
    history_list = {}
    history = {}
    hist = histories.query.filter().all()
    for h in hist:
        history = {
            'history_date': h.history_Date,
            'history_sale': h.total_sale,
            'history_quantity': h.total_ticket_quantity,
        }
        history_list[h.history_Id]=history
    return jsonify(history_list)

@app.route('/loggingOut', methods = ['GET'])
def log_out():
    checkcart = ticket.query.filter().all()
    for laman in checkcart:
        db.session.delete(laman)
        db.session.commit()
    return "logging out"


#Manage
@click.group(cls=FlaskGroup, create_app=lambda: app)
def web_cli():
    """
    Tool for managing the web application
    """


@web_cli.command('db')
def create_db():
    """
    Creates database tables
    """
    db.create_all()
    print('Database tables successfully created')


@web_cli.command()
def drop_db():
    """
    Drops all database tables
    """
    db.drop_all()
    print('Database tables successfully dropped')


if __name__ == '__main__':
    web_cli()

if __name__ == "__main__":
    app.run()
