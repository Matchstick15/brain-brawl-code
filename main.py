from flask import Flask, render_template, request, redirect, session
import sqlite3 as sql
app = Flask(__name__)
app.secret_key = "Brain_Brawl"

def create_user(username, password, school, year_level, fistname, lastname, subjects):
    print(f"insert user {username}")
    con = sql.connect("./Databases/main.db")
    cur = con.cursor()
    query = f"INSERT INTO Users (UserName, Password, School, YearLevel, FirstName, LastName, Subjects) values ('{username}','{password}','{school}','{year_level}','{fistname}','{lastname}','{subjects}');"
    print(query)
    data = cur.execute(query)
    print(f"Added user {username}")
    con.commit()
    con.close()
    return data

@app.route("/")
def mainpage():
    return render_template("main.html")

@app.route("/signup.html", methods=['POST', 'GET'])
def signuppage():
    print("signup page")
    if request.method == "POST":
        print("create user")
        username = request.form['UserName']
        create_user(
            username,
            request.form['Password'],
            request.form['School'],
            request.form['YearLevel'],
            request.form['FirstName'],
            request.form['LastName'],
            request.form['Subjects'],
        )
        session['user'] = username  # Store user in session
        return redirect("/home.html")    # Redirect to home
    else:
        print("Displaying")
        return render_template("signup.html", user=None)

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == "POST":
        username = request.form['UserName']
        password = request.form['Password']
        print(f"Trying login: {username} / {password}")
        con = sql.connect("./Databases/main.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM Users WHERE UserName=? COLLATE NOCASE AND Password=?", (username, password))
        user = cur.fetchone()
        print(f"DB result: {user}")
        con.close()
        if user:
            session['user'] = username
            return redirect("/home.html")
        else:
            error = "Invalid username or password"
    return render_template("login.html", error=error)

@app.route('/home.html')
def home():
    user = session.get('user')
    return render_template("home.html", user=user)

@app.route("/profile.html")
def profilepage():
    return render_template("profile.html")

@app.route("/quizes.html")
def quizpage():
    return render_template("quizes.html")

app.run(debug=True, port=5000)