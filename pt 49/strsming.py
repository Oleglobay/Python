from flask import Flask, redirect, render_template, make_response, request, url_for
from flask_socketio import SocketIO, emit
from flask_login import LoginManager, login_user
import json
import re
import os

import sqlite3
from models.person import  Person




class Person:

  def __init__(self, againUsername, intAgainPassword, email, age, aqqintAgainPassword, hobby = "I DONT HAE HOHBY"):
    self.againUsername = againUsername
    self.intAgainPassword =  intAgainPassword
    self.email = email
    self.age = age
    self.aqqintAgainPassword = aqqintAgainPassword
    self.hobby = hobby

  def speak(self, word):
    return self.againUsername + " says " + word

  def updateAge(self, age):
    self.age  = age

  def getAge(self):
   return self.age

  def getName(self):
   return self.againUsername

class News:
    def __init__(self, image, title, description):
        self.image = image
        self.title = title
        self.description = description





app = Flask(__name__)

app.config['secred_key'] = 'secret!'
socketio = SocketIO(app)

login_manager = loginManager(app)

@app.route("/Home")
def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def create_db ( ) :
    db = connect_db()
    with app.open_resource('sq_db.sql', mode = 'r') as f:
        db.cursor().executescript (f.read())
        db.commit()
        db.close()

def get_db():
    if not hasattr(g, 'link_bd'):
        g.link_db = connect_db()
        return g.link_db

@app.route("/Home")
def index():
    db = get_db()
    return render_template('home.html')

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()






@app.route("/")
def index1():
    return render_template("layout.html")

@app.route("/home")
def index2():
    return render_template("index.html")

@app.route("/Home")
def index3і():
    return render_template("home.html")

@app.route("/getcocue")
def getcocue():
    againUsername = request.cookie.get("againUsername")

@app.route("/cocue", methods=["POST", "GET"])
def cocue():
    if (request.method == 'POST'):
        if (request.form["againUsername"] == "unaskilol" and request.form["intAgainPassword"] == "unaskilol228"):
            return redirect("home")
        else:
            return render_template("farm.html")
    else:
        return render_template("farm.html")




@app.route('/register', methods=['POST','GET'])
def regist():
    if (request.method == 'POST'):

        checks = 0
        email = request.form['email']
        if temail.split("@")[1] in ["gmail.com", "ukr.net"]:
            checks += 1

        againUsername = request.form['againUsername']
        if tnickname.isalpha():
            checks += 1

        intAgainPassword = request.form['intAgainPassword']
        if (len(intAgainPassword) >= 8):
            plow = False
            pup = False
            pnum = False
            for letter in list(intAgainPassword):
                if letter.islower():
                    plow = True
                if letter.isupper():
                    pup = True
                if letter.isdigit():
                    pnum = True
            if (plow and pup and pnum):
                checks +=1

        aqqintAgainPassword = request.form['aqqintAgainPassword']
        if aqqintAgainPassword == intAgainPassword:
            checks += 1

        age = request.form['age']
        if int(age)>18:
            checks += 1

        if checks == 7:
            db = get_db()
            dbase = FDataBase(db)
            hash = generate_password_hash(tpassword)
            if not res:
                print("Error")
            else:
                print("Success")

            return redirect(url_for('index.html'))
        else:
            return render_template('aqqlogin.html')
    else:
        return render_template('aqqlogin.html')





if __name__ == "__main__":
    app.run(debug = True, port = 1201)
    create_db()