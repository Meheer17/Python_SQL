from flask import Flask, redirect, url_for, render_template, request
import function as sql

app = Flask(__name__)

if sql.headers[0] == 1:
    auth = True
else:
    auth = False

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", page='login')

@app.route("/jasdb", methods=["GET","POST"])
def home():
    return render_template("index.html", page='login')

if __name__ == "__main__":
	app.run()
    