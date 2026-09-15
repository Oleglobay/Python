from flask import Flask, redirect, render_template, make_response, request, url_for

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



if __name__ == "__main__":
    app.run(debug = True, port = 1201)