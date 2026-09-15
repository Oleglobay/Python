from flask import *
app = Flask(__name__)

@app.route('/1234')
def index():
	return render_template("index.html")

@app.route('/login',methods=['POST','GET'])
def login():
	if (request.method == 'POST'):
		print('Post')
		email = request.form['email']
		name = request.form['name']
		password = request.form['password']
		sex = request.form['s']
		n = request.form['news']
		print(email, name, password, sex, n)
		return redirect(url_for("index"))
	else:
		return render_template('login.html')


if __name__ == '__main__':
	app.run(port=1000)
