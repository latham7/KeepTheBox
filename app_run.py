from flask import Flask, render_template
from calculate.views import calculateRoute
import sqlite3


# App Imports
app = Flask(__name__, template_folder='web/templates', static_folder='web/static')
version = "1.1.1"

app.add_url_rule('/calculate', 'calculateRoute', calculateRoute)
@app.route("/", methods=['GET', 'POST']) ## This index is weird. It will be a login page at some point
def index():
    return render_template("index.html", 
    version=version)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)