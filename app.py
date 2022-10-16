from flask import Flask, render_template, request
from calculate import calculate

import sqlite3


# App Imports
app = Flask(__name__, template_folder='web/templates', static_folder='web/static')
version = "1.1.1"

@app.route("/", methods=['GET', 'POST']) ## This index is weird. It will be a login page at some point
def index():
    return render_template("index.html", 
    version=version)


@app.route('/calculate', methods=['GET', 'POST'])
def calculateRoute():
    goldValueDebug = int(request.form.get('gold-amount'))
    print(goldValueDebug)
    try:
        goldValue = int(request.form.get('gold-amount'))
        ironValue = int(request.form.get('iron-amount'))
        coalValue = int(request.form.get('coal-amount'))
        copperValue = int(request.form.get('copper-amount'))
        total = calculate(goldValue, ironValue, coalValue, copperValue)
        return render_template("index.html", version=version, total=total)
    except ValueError: #TypeError:
        print("0001 - Could not convert string to int")
        return render_template("index.html", version=version, total="ERROR: Please enter a number.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)