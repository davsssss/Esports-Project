from flask import Flask, render_template, jsonify   
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/introduction")
def introduction():
    return render_template("introduction.html")

@app.route("/LOL")
def LOL():
    return render_template("Models.html")

@app.route("/Valorant")
def Valorant():
    return render_template("ValPredictions.html")

@app.route("/Queries")
def Queries():
    return render_template("SQLQueries.html")

if __name__ == "__main__":
    app.run(debug=True)