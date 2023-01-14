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

if auth == False:
    @app.route("/login", methods=["GET","POST"])
    def login():
        if request.method == 'GET':
            return render_template("login.html", page='LOGIN', auth = auth)
        else:
            sql.Login(request.form['Email'], request.form['Password'])

    @app.route("/signup", methods=["GET","POST"])
    def signup():
        if request.method == 'GET':
            return render_template("login.html", page='SIGNUP', auth = auth)
        else:
            sql.Login(request.form['Email'], request.form['Password'])
else:
    def retrn():
        return redirect("/")

if __name__ == "__main__":
	app.run()
    