from flask import Flask
app = Flask(__name__)


@app.route("/home/unaskilol")
def index():
    return '<h1>я хочу пельмені</h1>'

@app.route("/about/unaskilol")
def index2():
    return '<h1>я k.,kz gtkmvtys s anime girl</h1>'

@app.route("/users/home")
def index3():
    return '<h1>ніші юзери sergey sergey2 sergey3</h1>'

@app.route("/user/1")
def index4():
    return '<h1>sergey харош</h1>'

@app.route("/user/2")
def index5():
    return '<h1>sergey2 не приятна людина</h1>'

@app.route("/user/3")
def index6():
    return '<h1>sergey3 коля </h1>'

if __name__=='__main__':
    app.run(debug=True)
