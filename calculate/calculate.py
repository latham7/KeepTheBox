from flask import Flask, render_template, request, redirect

from main import app
version = "1.1.1"

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

def calculate(gold, iron, coal, copper):
    goldOutput = gold*2275
    ironOutput = iron*2275
    coalOutput = coal*2275
    copperOutput = copper*2275

    total=goldOutput+ironOutput+coalOutput+copperOutput
    return total
