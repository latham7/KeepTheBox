from flask import Flask, render_template, request, redirect
import calculate.calculate
import sqlite3


# App Imports

app = Flask(__name__, template_folder='web/templates', static_folder='web/static')
version = "1.1.1"

@app.route("/", methods=['GET', 'POST']) ## This index is weird. It will be a login page at some point
def index():
    return render_template("index.html", 
    version=version)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)