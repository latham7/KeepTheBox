from flask import Flask, render_template, request, redirect
from func.calculate import calculate

app = Flask(__name__)

version = 1.2

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html", version=version)

@app.route('/calculate')
def calculateRoute():
    goldValue = int(request.args.get('gold-amount'))
    ironValue = int(request.args.get('iron-amount'))
    coalValue = int(request.args.get('coal-amount'))
    copperValue = int(request.args.get('copper-amount'))

    total = calculate(goldValue, ironValue, coalValue, copperValue)
    print(type(total))
    return render_template("index.html", version=version, total=total)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)