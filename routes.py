from flask import Flask, redirect, url_for, render_template, request
import function as sql

app = Flask(__name__)


@app.route('/', methods=['GET'])
def reroute():
    return redirect(url_for("home"))

@app.route("/home", methods=["GET"])
def home():
    return render_template("index.html", auth = sql.Auth())


@app.route("/login", methods=["GET","POST"])
def login():
    if sql.Auth() == False:
        if request.method == 'GET':
            return render_template("login.html", page='LOGIN', auth = sql.Auth())
        elif request.method == "POST":
            sql.Login(request.form['email'], request.form['password'])
            return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/')

@app.route("/signup", methods=["GET","POST"])
def signup():
    if sql.Auth() == False:
        if request.method == 'GET':
            return render_template("login.html", page='SIGNUP',  auth = sql.Auth())
        elif request.method == "POST":
            sql.SignUp(request.form['email'], request.form['password'])
            return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/')

@app.route("/database", methods=["GET","POST"])
def Display_Tables():
    data = sql.ShowTable()
    print(request)
    if request.args.get("tn"):
        args = request.args.get("tn")
        desc = sql.DesTable(args)
        disdat = sql.DisplayAll(args)
        return render_template('database.html',auth= sql.Auth(), tables=data, desc=desc, disdat=disdat)
    else: 
        return render_template('database.html', tables=data)

@app.route("/update-database", methods=["GET","POST"])
def updatepg():
    data = sql.ShowTable()
    print(request)
    if request.args.get("tn"):
        args = request.args.get("tn")
        desc = sql.DesTable(args)
        disdat = sql.DisplayAll(args)
        return render_template('update.html',auth= sql.Auth(), tables=data, desc=desc, disdat=disdat)
    else: 
        return render_template('update.html', tables=data)

def ret():
    return redirect(url_for("home"))

if __name__ == "__main__":
	app.run()
    