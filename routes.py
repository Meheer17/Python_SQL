from flask import Flask, redirect, url_for, render_template, request
# import function as sql

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", page='login')

if __name__ == "__main__":
	app.run()
    