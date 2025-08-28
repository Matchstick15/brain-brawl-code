from flask import Flask, render_template

app = Flask (__name__)
app.secret_key = "Brain_Brawl"

@app.route("/")
def homepage():
    return render_template("main.html")

@app.route("/signup.html")
def signuppage():
    return render_template("signup.html")

@app.route("/login.html")
def loginpage():
    return render_template("login.html")

app.run(debug=True, port=5000)