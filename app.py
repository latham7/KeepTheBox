from flask import Flask, render_template, request, redirect
from calculate import calculate
from database import createUser, initDb
import logging
import sqlite3

# TODO Get SQLite3 working with user database


app = Flask(__name__, template_folder='web/templates', static_folder='web/static')
version = "1.2"

debug_mode = False  # TODO Implement debugging mode


####### INDEX APP ROUTE #################
@app.route("/", methods=['GET', 'POST'])  ## This index is weird. It will be a login page at some point
def index():
    # if has permission, return index.html
    # if not has permission, return login.html
    return render_template("index.html",
                           version=version)


####### LOGIN APP ROUTE #################
@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    initDb()
    # createUser(username, password)
    try:
        createUser(username, password)
        return render_template('index.html')
    except:
        return render_template('login.html')

    # return render_template('login.html')


####### CALCULATE APP ROUTE #################
@app.route('/calculate', methods=['GET', 'POST'])
def calculateRoute():
    try:
        payoutInt = 65
        goldValue = int(request.form.get('gold-amount'))
        ironValue = int(request.form.get('iron-amount'))
        coalValue = int(request.form.get('coal-amount'))
        copperValue = int(request.form.get('copper-amount'))
        payoutInt = int(request.form.get('payoutPercent'))
        total = calculate(goldValue, ironValue, coalValue, copperValue, payoutInt)
        return render_template("index.html", version=version, total=total, payoutPercent=payoutInt)
    except (ValueError, TypeError, NameError):
        logging.error("Error, lol, figure it out")
        print("0001 - Could not convert string to int")
        return render_template("index.html", version=version, total="Error")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
