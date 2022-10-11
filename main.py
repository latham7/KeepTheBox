from flask import Flask, render_template, request, redirect



app = Flask(__name__)

version = 1.1

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html", version=version)

@app.route('/calculate')
def calculate():
    goldValue = int(request.args.get('gold-amount'))
    ironValue = int(request.args.get('iron-amount'))
    coalValue = int(request.args.get('coal-amount'))
    copperValue = int(request.args.get('copper-amount'))

    goldOutput = goldValue*2275
    ironOutput = ironValue*2275
    coalOutput = coalValue*2275
    copperOutput = copperValue*2275

    total=goldOutput+ironOutput+coalOutput+copperOutput



    return render_template("index.html", version=version, total=total)

@app.route('/goldCalculate')
def goldCalculate():
    goldValue = int(request.args.get('gold-amount'))
    goldOutput = goldValue*2275
    return render_template("index.html", version=version, goldValueOutput=goldOutput)


@app.route('/ironCalculate')
def ironCalculate():
    ironValue = int(request.args.get('iron-amount'))
    ironOutput = ironValue*2275
    return render_template("index.html", version=version, ironValueOutput=ironOutput)

@app.route('/coalCalculate')
def coalCalculate():
    coalValue = int(request.args.get('coal-amount'))
    coalOutput = coalValue*2275
    return render_template("index.html", version=version, coalValueOutput=coalOutput)

@app.route('/copperCalculate')
def copperCalculate():
    copperValue = int(request.args.get('copper-amount'))
    copperOutput = copperValue*2275
    return render_template("index.html", version=version, copperValueOutput=copperOutput)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)