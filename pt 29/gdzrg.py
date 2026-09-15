from flask import Flask
app = Flask(__name__)

@app.route("/1234")
def index():
        return render_template("index.html")

if __name__=='__main__':
        app.run(port=777)
