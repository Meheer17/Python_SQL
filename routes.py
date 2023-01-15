from flask import Flask, redirect, url_for, render_template, request
import function as sql

app = Flask(__name__)


@app.route('/', methods=['GET'])
def reroute():
    return redirect(url_for("home"))

@app.route("/home", methods=["GET"])
def home():
    return render_template("index.html", auth = sql.Auth())

if sql.Auth() == False:
    @app.route("/login", methods=["GET","POST"])
    def login():
            if request.method == 'GET':
                return render_template("login.html", page='LOGIN', auth = sql.Auth())
            elif request.method == "POST":
                sql.Login(request.form['email'], request.form['password'])
                return redirect('/')
            else:
                return redirect('/')

    @app.route("/signup", methods=["GET","POST"])
    def signup():
            if request.method == 'GET':
                return render_template("login.html", page='SIGNUP', auth = sql.Auth())
            elif request.method == "POST":
                sql.SignUp(request.form['email'], request.form['password'])
                return redirect('/')
            else:
                return redirect('/')

elif sql.Auth() == True:
    @app.route("/database", methods=["GET","POST"])
    def Display_Tables():
            data = sql.ShowTable()
            if desc:
                args = request.args.to_dict().get("Table_number")
                desc = sql.DesTable(args)
                return render_template('database.html', tables=data, desc=desc)
            else: 
                return render_template('database.html', tables=data)
else:
    def ret():
        return redirect(url_for("home"))

if __name__ == "__main__":
	app.run()
    