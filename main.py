from flask import Flask, render_template,request 
import sqlite3 as sql
app = Flask (__name__)
app.secret_key = "Brain_Brawl"

# current_user = ""

@app.route("/")
def homepage():
    return render_template("main.html")


def create_user(username,password,school,year_level,fistname,lastname,subjects):
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

@app.route("/test", methods=["POST"])
def test():
    print("Test")


@app.route("/signup.html", methods = ['POST','GET'])
def signuppage():
    print("signup page")
    if request.method=="POST":
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
        # current_user = username
        return render_template('/signup.html', is_done=True, user = username)
    else:   
        print("Displaying")
        return render_template("signup.html", user = None)

@app.route("/login.html")
def loginpage():
    return render_template("login.html")

app.run(debug=True, port=5000)