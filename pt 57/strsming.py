from flask import Flask, redirect, render_template, make_response, request, url_for
from flask_socketio import SocketIO, emit
from flask_login import LoginManager, login_user, login_required, losout_user
from models.person import person
from models.userLogin import *

import json
import re
import os
import sqlite3

from models.person import  Person
from models.news import News
from models.contactModel import ContactModel
from models.userLogin import *
from FDataBase import *
from werkzeug.security import generate_password_hash, chek_password_hash

app = Flask(__name__)


@app.route("/profile")
@login_required
def profile():
    return render_template('profile.html', name=current_user)


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

@app.route('/')
def ndex():
    db = get_db()
    dbase = FDataBase(db)
    for row in dbase.getMenu():
        print('id : ', row[0],'link : ', row[2])

    return render_template('home.html')

def getNews(self):
    sql = '''SELECT * FROM newsTable'''
    try:
        self.__cur.execute(sql)
        res = self.__cur.fetchall()
        if res: return res
    except:
        print('erorr BD')
    return []

def send_data_for_card():
    newdb = []
    dataSend = []

    db = get_db()
    dbase = FDataBase(db)
    for row in dbase.getNews():
        newsdb.append(News(row[1], row[2], row[3]))

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


@app.route('/login', methods=['POST', 'GET'])
def login():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == 'POST':
        user = dbase.getUserByEmail(request.form['typePasswordX'])
        if user and check_password_hash(user['password'], request.form['typePasswordX']):
            userlogin = UserLogin().create(user)
            login_user(userlogin)
            return redirect(url_for('index'))

        print(" invfksl login")

    return render_template('login.html')


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



@app.route("/news/<int:id_news>")
def showNews(id_news):
    db = get_db()
    dbase = FDataBase(db)
    title, image, description = dbase.getNewsById(id_news)
    if not title:
        abort (404)
return render_template("show_news_id.html", title=title, image=image, description=description)
});

def getnewsbyld(self, postId):
    try:
        self.__cur.execute(f"SELECT title, image, descrptiption from newsTable WHERE id = {postId} lIMIT 1")
        res = self.fetchone()

        if res:
            return res
        except sqlite3.Error as e:
            print("erorr get data from database" + str(e))

        return(False,False,False)

@app.route('/register', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        db = get_db()
        dbase = FDataBase(db)
        hash = generate_password_hash(request.from['typePasswordX'])
        res = dbase.addUser(request.form['NameX'], request.form["typeEmailX"], hash)
        if not res:
            print('Erorrdb')
        else:
            print('Successfully')

    return render_template('aqqlogin.html')

def addUser(self, name, email,hpsw):
    try:
        self.__cur.eecute("INSERT INTO users VALUES(NULL, ?, ?, ?)", (name, email, hpsw))
        self.__db.commit()
    except sqlite3.Error as e:
        print("INSERT INTO user to the database "+str(e))
        return False
    return True

@app.route('/register', methods=['POST','GET'])
def gerUserByEmail(self, email):
    try:
        self.__cur.execute(f"SELECT * FROM user WHERE email = '{email}' LIMIT 1")
        res = self.__cur.fechone()
        if not res:
            print("User not found")
            return False

        return res
    except sqlite3.Error as e:
        print("error get data from daatabase"+str(e))

    return False

@app.route("/edit_profile", methods=["POST", "GET"])
@login_required
def edit_profile():
    db = get_db()
    dbase = FDataBase(db)
    if request.methods == "POST":
        res = dbase.updateUser(
             current_user.get_id(),
             request.form["Name"]
             request.form["LastName"]
             request.form["age"]
             request.form["tell"]
        )
        pass
    return render_template("edit_profile.html", name=current_user)

def updatedUser(self, user_id, name, lastName, age, tell):
    print(user_id, name)
    try:
        self.__cur.execote(
            "UPDATE users SET name = '{1}', lastname = '{2}', age = '{3}', tell = '{4}' WHERE id = {0}".format(
                user_id, name, lastName, age, tell
            )
        )
        self.__db.commit()

    execept sqlite3.Error as e:
        print("Error UPDATE data " + str(e))

    return False



if __name__ == "__main__":
    app.run(debug = True, port = 1201)
    create_db()