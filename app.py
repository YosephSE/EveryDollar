from flask import Flask, request, render_template, redirect, url_for
from flask_mysqldb import MySQL
from datetime import datetime
from decimal import Decimal

# Initialize flask
app = Flask(__name__)
app.secret_key = 'TzALB4eJ89*Ib!bn0aH28w9MFSy2iuu1!0olxkHADk2gq&PpMQ'

# Connect to MYSQL database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1212'
app.config['MYSQL_DB'] = 'everydollar'
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

# Initialize the Connection
mysql = MySQL(app)

@app.route("/")
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM saving ORDER BY id DESC LIMIT 10")
    saving = cur.fetchall()
    cur.execute("SELECT * FROM cash ORDER BY id DESC LIMIT 10")
    cash = cur.fetchall()
    cur.execute("SELECT * FROM loan ORDER BY id DESC LIMIT 10")
    loan = cur.fetchall()
    cur.close()
    return render_template("index.html", saving = saving, cash = cash, loan = loan)

@app.route("/addSaving", methods=["GET", "POST"])
def addSaving():
    if request.method == "POST":
        cur = mysql.connection.cursor()
        cur.execute("SELECT amount FROM saving ORDER BY id DESC LIMIT 1")
        amount = cur.fetchall()[0]['amount']
        income = request.form["income"]
        reason = request.form["reason"]
        amount += Decimal(float(income))
        cur.execute("INSERT INTO saving (transaction, reason, amount, date) VALUES (%s, %s, %s, %s)",(income, reason, amount, datetime.now().strftime("%Y-%m-%d")))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for("home"))
    return render_template('addSaving.html')


    
    


@app.route("/subSaving", methods=["GET", "POST"])
def subSaving():
    if request.method == "POST":
        cur = mysql.connection.cursor()
        cur.execute("SELECT amount FROM saving ORDER BY id DESC LIMIT 1")
        amount = cur.fetchall()[0]['amount']
        expense = Decimal(float(request.form["expense"])) * (-1)
        reason = request.form["reason"]
        amount += expense
        cur.execute("INSERT INTO saving (transaction, reason, amount, date) VALUES (%s, %s, %s, %s)",(expense, reason, amount, datetime.now().strftime("%Y-%m-%d")))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for("home"))
    return render_template("subSaving.html")



@app.route("/addCash", methods=["GET", "POST"])
def addCash():
    if request.method == "POST":
        cur = mysql.connection.cursor()
        cur.execute("SELECT amount FROM cash ORDER BY id DESC LIMIT 1")
        amount = cur.fetchall()[0]['amount']
        income = request.form["income"]
        reason = request.form["reason"]
        amount += Decimal(float(income))
        cur.execute("INSERT INTO cash (transaction, reason, amount, date) VALUES (%s, %s, %s, %s)",(income, reason, amount, datetime.now().strftime("%Y-%m-%d")))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for("home"))
    return render_template('addCash.html')


    
    


@app.route("/subCash", methods=["GET", "POST"])
def subCash():
    if request.method == "POST":
        cur = mysql.connection.cursor()
        cur.execute("SELECT amount FROM cash ORDER BY id DESC LIMIT 1")
        amount = cur.fetchall()[0]['amount']
        expense = Decimal(float(request.form["expense"])) * (-1)
        reason = request.form["reason"]
        amount += expense
        cur.execute("INSERT INTO cash (transaction, reason, amount, date) VALUES (%s, %s, %s, %s)",(expense, reason, amount, datetime.now().strftime("%Y-%m-%d")))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for("home"))
    return render_template("subCash.html")



@app.route("/addLoan", methods=["GET", "POST"])
def addLoan():
    if request.method == "POST":
        cur = mysql.connection.cursor()
        cur.execute("SELECT amount FROM loan ORDER BY id DESC LIMIT 1")
        amount = cur.fetchall()[0]['amount']
        income = request.form["income"]
        reason = request.form["reason"]
        amount += Decimal(float(income))
        cur.execute("INSERT INTO loan(transaction, reason, amount, date) VALUES (%s, %s, %s, %s)",(income, reason, amount, datetime.now().strftime("%Y-%m-%d")))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for("home"))
    return render_template('addLoan.html')


    
    


@app.route("/subLoan", methods=["GET", "POST"])
def subLoan():
    if request.method == "POST":
        cur = mysql.connection.cursor()
        cur.execute("SELECT amount FROM loan ORDER BY id DESC LIMIT 1")
        amount = cur.fetchall()[0]['amount']
        expense = Decimal(float(request.form["expense"])) * (-1)
        reason = request.form["reason"]
        amount += expense
        cur.execute("INSERT INTO loan (transaction, reason, amount, date) VALUES (%s, %s, %s, %s)",(expense, reason, amount, datetime.now().strftime("%Y-%m-%d")))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for("home"))
    return render_template("subLoan.html")

if __name__ == "__main__":
    app.run(debug=True)