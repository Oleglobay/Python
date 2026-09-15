from flask import *
from flask_socketio import *
from flask_login import *
import json
import re123
import os
import sqlite3


from models.person import Person
from models.news import News
from models.contact import Contact
from FDataBase import *
form werkzeug.secuity import generate_password_hash, check_password_hash
class UserLogin:
	def fromDB(self, user_id, db):
		self.__user = db.getUser(user_id)
		return self

	def create(self,user):
		self.__user = user
		return self

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return str(self.__user['id'])

	def get_nick(self):
		return str(self.__user['fname'])

	def get_firstName(self):
		return str(self.__user['fname'])

	def get_lastName(self):
		return str(self.__user['sname'])

	def get_age(self):
		return str(self.__user['age'])

	def get_email(self):
		return str(self.__user['email'])

	def get_tell(self):
		return str(self.__user['tell'])

#database
peopleDB = []


DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY = 'dgjkaoeijhnvkrnmvklowfo'
USERNAME = 'admin'
PASSWORD = '123'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

login_manager = LoginManager(app)

def connect_db():
	conn = sqlite3.connect(app.config['DATABASE'])
	conn.row_factory = sqlite3.Row
	return conn

def create_db():
	db = connect_db()
	with app.open_resource('sq_db.sql', mode = 'r') as f:
		db.cursor().executescript (f.read())
	db.commit()
	db.close()

def get_db():
	if not hasattr(g, 'link_db'):
		g.link_db = connect_db()
	return g.link_db

@app.teardown_appcontext
def close_db(error):
	if hasattr(g, ' link_db'):
		g.link_db.close()


def send_data_for_card():
	newsdb = []
	dataSend = []

	db = get_db()
	dbase = FDataBase(db)
	for row in dbase.getNews():
		newsdb.append(News(row[0],row[1],row[2],row[3]))
	for news in newsdb:
		dataSend.append(json.dumps(news.__dict__))
	return dataSend

def send_data_for_contact():
	contdb = []
	dataSend = []

	db = get_db()
	dbase = FDataBase(db)
	for row in dbase.getContact():
		contdb.append(Contact(row[0],row[1],row[2],row[3]))
	for contact in contdb:
		dataSend.append(json.dumps(contact.__dict__))
	return dataSend
@socketio.on('my_eve')
def sendDB(json):
	print(json)
	if (json["data"] == "/about"):
		emit('sendContact', send_data_for_contact())
	elif(json["data"] == "/news"):
		emit('sendNews', send_data_for_card())

@app.route('/')
def home():
	return render_template("main.html")

@app.route('/empty')
def empty():
	return render_template("empty.html")

@app.route('/contact')
def contact():
	return render_template("contact.html")

@app.route("/user")
@login_required
def use():
	db = get_db()
	dbase = FDataBase(db)
	if request.method == "POST":
		res = dbase.updatedUser(
			current_user.get_id()
			request.form["nickname"]
			request.form["fName"]
			request.form["sName"]
			request.form["email"]
			request.form["age"]
			)
	return render_template("user.html", name=current_user)

@app.route("/news")
def news():
	return render_template("news.html")

@app.route('/news/add', methods=['POST','GET'])
def newsadd():
	db = get_db()
	dbase = FDataBase(db)

	if (request.method == 'POST'):
		if len(request.form['name']) > 4 and len(request.roem['post']) > 10
			res = dbase.addNews(request.form['imageLink'],request.form['name'],request.form['post'])
			if not res:
				print("Error DB")
			else:
				print("Sucessfully")
	else:
		return render_template('addnews.html')

@app.route("news/<int:id_news>")
def showNews(id_news):
	db = get_db()
	dbase = FDataBase(db)
	title, image, description = dbase.getNewsById(id_news)
	if not title:
		abort(404)
	return render_template("shownews.html", title=title, image=image, description=description)

@app.route('/register', methods=['POST','GET'])
def regist():
	if (request.method == 'POST'):

		checks = 0
		temail = request.form['email']
		if temail.split("@")[1] in ["gmail.com", "ukr.net"]:
			checks += 1

		tnickname = request.form['nickname']
		if tnickname.isalpha():
			checks += 1

		tpassword = request.form['password']
		if (len(tpassword) >= 8):
			plow = False
			pup = False
			pnum = False
			for letter in list(tpassword):
				if letter.islower():
					plow = True
				if letter.isupper():
					pup = True
				if letter.isdigit():
					pnum = True
			if (plow and pup and pnum):
				checks +=1

		taPassword = request.form['againPassword']
		if taPassword == tpassword:
			checks += 1

		tfName = request.form['fName']
		if tfName.isalpha() and tfName[0].isupper() and tfName[1:].islower():
			checks += 1

		tsName = request.form['sName']
		if tsName.isalpha() and tsName[0].isupper() and tsName[1:].islower():
			checks += 1

		tage = request.form['age']
		if int(tage)>18:
			checks += 1

		if checks == 7:
			people = Person(fName = tfName, sName = tsName, nickname = tnickname, email = temail, password = taPassword, age = tage)
			db = get_db()
			dbase = FDataBase(db)
			hash = generate_password_hash(tpassword)
			res = dbase.addUser(tnickname, temail, hash, tfName, tsName, tage)
			if not res:
				print("Error")
			else:
				print("Success")

			return redirect(url_for('login'))
		else:
			return render_template('regist.html')
	else:
		return render_template('regist.html')

@app.route('/login', methods=['POST','GET'])
def login():
	db = get_db()
	dbase = FDataBase(db)
	if (request.method == 'POST'):
		user = dbase.getUserByEmail(request.form["email"])
		if user and check_password_hash(user['password'], request.form['password']):
			userlogin = UserLogin().create(user)
			login_user(userlogin)
			return redirect(url_for(''))
		print("invalid")
	return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect("login")

@login_manager.user_loader
def load_user(user_id):
	print("load_user")
	db = get_db()
	dbase = FDataBase(db)
	return UserLogin().fromDB(user_id, dbase)

if __name__ == '__main__':
	socketio.run(app, port=1000)
