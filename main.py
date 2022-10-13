from ast import While
from flask import Flask, render_template, request, redirect
from func.calculate import calculate

app = Flask(__name__)

version = "1.1.1"

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html", version=version)

@app.route('/calculate')
def calculateRoute():
    try:
        goldValue = int(request.args.get('gold-amount'))
        ironValue = int(request.args.get('iron-amount'))
        coalValue = int(request.args.get('coal-amount'))
        copperValue = int(request.args.get('copper-amount'))
        total = calculate(goldValue, ironValue, coalValue, copperValue)
        return render_template("index.html", version=version, total=total)
    except ValueError:
        print("0001 - Could not convert string to int")
        return render_template("index.html", version=version, total="ERROR: Please enter a number.")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)