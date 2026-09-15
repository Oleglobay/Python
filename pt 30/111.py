from flask import *
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/login",  methods=["POST", "GET"])
def login():
    if request.method == "POST":
        if(request.form["username"] == "unaskilol" and
           request.form["password"] == "228"):
            return render_template("index.html")
        else:
            return render_template("login22.html")

if __name__ == '__main__':
 app.run(debug = True, port = 777) 
