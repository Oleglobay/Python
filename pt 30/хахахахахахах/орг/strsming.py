from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        if (request.form["username"] == "unaskilol" and
            request.form["password"] == "unaskilol228"):
            return render_template("/index.html")
        else:
            print("Invalid username/password")
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug = True, port = 477)
