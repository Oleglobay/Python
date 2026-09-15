from flask import*
app = Flask(__name__)

@app.route("/")
def index():
    return render(url_for("login"))

@app.route("/login", methobs=["POST", "GET"])
def login():
    if request.method == "POST":
        if (request.form["username"] == "unaskilol" and
            request.form["password"] == "unaskilol228"):
            return render_template("/index.html")
        else:
            abort(401)
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug = True, port = 478)
