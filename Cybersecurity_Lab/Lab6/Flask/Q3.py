from flask import Flask
app = Flask(__name__)
@app.route("/")
def simplepage():
    return "<p>Team 4: Graham Filip and McCarthy Tom</p>"