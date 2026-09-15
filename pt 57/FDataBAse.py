import sqlite3

class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getMenu(self):
        sql - '''SELECT * FROM mainmenu'''
        try:
            srlf.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print('erorr DB')
        return[]

class UserLogin:
    def fromDB(self, user_id, db):
        self.__user = db.getUser(user_id)
        return self

    def create(self, user):
        self.__user = user
        return self

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def get_id(self):
        return str(self.__user['id'])

    def get_name(self):
        return str(self.__user['name'])

    def get_lastName(self):
        return str(self.__user['lastName'])

    def get_age(self):
        return str(self.__user['age'])\

@app.route("/add_news", methods=["POST","GET"])
def addnews
   db = get_db()
    dbase = FDataBase(db)

    if request.method == "POST":
        if len(request.from["name"]) > 4 and len(request.form["post"]) > 10:
        res = dbase.addnews(
            request.form["imageLink"], request.form["name"], request.form["post"], current_user.get_id()
        )
            if not res:
                print("erorr db")
            else:
                print("seccesfulyl")
        else:
           print("erroo")

   return render_template("fulldocumetn.html")

def addnews(self, imgUrl, title, description):
    try:
        self.__cur.execute(
            "INSERT INTO newsTable VALUES(NULL, ?, ?, ?)",
            (imgurl, title, description),
        )
        self.__db.commit()
    except sqlite3.Error as e:
        print("ошибка статі в бд"+str(e))
        return False

    return True

