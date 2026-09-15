from flask import Flask, render_template, url_for,request

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if (request.method == 'POST'):
        againUsername = request.form["againUsername"]
        if (request.form["againUsername"] == "unaskilol" and
            request.form["intAgainPassword"] == "unaskilol228"):
            return url_for("home")
        else:
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug = True, port = 1200)
