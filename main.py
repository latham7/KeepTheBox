from flask import Flask, render_template, request, redirect



app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html",)

@app.route('/goldCalculate')
def goldCalculate():
    goldValue = request.args.get('gold-amount')
    goldValueInt = int(goldValue)
    goldValueOutput = goldValueInt*2275



    return render_template("index.html", goldValueOutput=goldValueOutput)

@app.route('/ironCalculate')
def ironCalculate():
    ironValue = request.args.get('iron-amount')
    ironValueInt = int(ironValue)
    ironValueOutput = ironValueInt*2275
    return render_template('index.html', ironValueOutput=ironValueOutput)

@app.route('/coalCalculate')
def coalCalculate():
    coalValue = request.args.get('coal-amount')
    coalValueInt = int(coalValue)
    coalValueOutput = coalValueInt*2275
    return render_template('index.html', coalValueOutput=coalValueOutput)

@app.route('/copperCalculate')
def copperCalculate():
    copperValue = request.args.get('copper-amount')
    copperValueInt = int(copperValue)
    copperValueOutput = copperValueInt*2275
    return render_template('index.html', copperValueOutput=copperValueOutput)

if __name__ == '__main__':
    app.run(host='0.0.0.0')