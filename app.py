
## Imports
from django.shortcuts import render
from flask import Flask, make_response, render_template, request, redirect, url_for
from calculate import calculate
from database import createUser, initDb
from auth import checkAuth, checkCookie
import logging
import sqlite3

app = Flask(__name__, template_folder='web/templates', static_folder='web/static')
version = "2.1"
debug_mode = False  # TODO Implement debugging mode
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

####### INDEX APP ROUTE #################
@app.route("/", methods=['GET', 'POST'])  
def index():
    createUser("test", "123")
    hasCookie = checkCookie(request.cookies.get('logonID'))
    if hasCookie:
        return redirect('/calculate')
    else: 
        return render_template('login.html')


####### LOGIN APP ROUTE #################
@app.route('/login', methods=['GET', 'POST'])
def login():
    cookie = request.cookies.get('logonID')
    hasCookie = checkCookie(cookie)
    if hasCookie:
        return render_template("index.html")
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        authed = checkAuth(username, password)
        if authed:
            resp = make_response(redirect('/calculate'))
            resp.set_cookie('logonID', username)
            return resp
            #return redirect(url_for("calculateRoute", next=request.url))
        else:
            return render_template('loginError.html', error="Incorrect Username or Password")

####### CALCULATE APP ROUTE #################
@app.route('/calculate', methods=['GET', 'POST'])
def calculateRoute():
    cookie = request.cookies.get('logonID')
    hasCookie = checkCookie(cookie)
    payoutInt = 50 ## TODO payout percent on the website defaults to 50, regardless of that value
    if hasCookie:
        try:
            goldValue = int(request.form.get('gold-amount'))
            ironValue = int(request.form.get('iron-amount'))
            coalValue = int(request.form.get('coal-amount'))
            copperValue = int(request.form.get('copper-amount'))
            gunpowderValue = int(request.form.get('gunpowder-amount'))
            netherwartValue = int(request.form.get('netherwart-amount'))
            dirtValue = int(request.form.get('dirt-amount'))
            deepslateValue = int(request.form.get('deepslate-amount'))            
            payoutInt = int(request.form.get('payoutPercent'))
            total = calculate(goldValue, ironValue, coalValue, copperValue, payoutInt, gunpowderValue, netherwartValue, dirtValue, deepslateValue)
            return render_template("index.html", version=version, total=total, payoutPercent=payoutInt)
        except (ValueError, TypeError, NameError):
            return render_template("index.html", version=version, total="Error", payoutPercent=payoutInt)
    else: return redirect('/')


@app.route('/error', methods=['GET', 'POST'])
def error():
    return render_template("error.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
