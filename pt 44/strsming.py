from flask import Flask, redirect, render_template, make_response, request, url_for

class Person:

  def __init__(self, againUsername, intAgainPassword, email, )





app = Flask(__name__)

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