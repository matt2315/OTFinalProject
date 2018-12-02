from flask import Flask, request, jsonify, url_for
from model import *
import datetime

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
    sQuantity = payload.get('silipQuantity', None)
    checker = ticket.query.filter(ticket.mTitle == 'Silip' ).first()
    if checker:
        newTix = ticket(mTitle = 'Silip', tQuantity = sQuantity, tPrice = ticket.tPrice + 50, tDatePurchased = datetime.datetime.now().date())
        db.session.add(newTix)
        db.session.commit()
        return "Silip ticket added"
    else:
        newTix = ticket(mTitle = 'Silip', tQuantity = sQuantity, tPrice = 50, tDatePurchased = datetime.datetime.now().date())
        db.session.add(newTix)
        db.session.commit()
        return "Silip ticket reserved"


if __name__ == "__main__":
    app.run()
