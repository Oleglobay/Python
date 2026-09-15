import sqlite3
class FDataBase:
	def __init__(self, db):
		self.__db = db
		self.__cur = db.cursor()

	def getContact(self):
		sql = '''SELECT * FROM contactTable'''
		try:
			self.__cur.execute(sql)
			res = self.__cur.fetchall()
			if res: return res
		except:
			print("Error with read DB")
		return []
	def getNews(self):
		sql = '''SELECT * FROM newsTable'''
		try:
			self.__cur.execute(sql)
			res = self.__cur.fetchall()
			if res: return res
		except:
			print("Error with read DB")
		return []
		
	def addNews(self, image, title, description):
		try:
			self.__cur.execute("INSERT INTO newstable VALUES(NULL, ?, ?, ?)"), (image, title,description)
			self.__db.commit()
			print("Python Variables inserted successfully into SqliteDb_developers table")
		except sqlite3.Error as e:
			print(e)
			return False

		return(True)
	def getNeswById(self, postId):
		try:
			self.__cur.execute(f"SELECT title, image, description FROM newstable WHERE id = {postId} LIMIT 1")
			res = self.__cur.fetchone()
			if res:
				return res
		except sqlite3.Error as e:
			print(e)
		return(False, False, False)

	def addUser(self, nick, email, hash, fname, sname, age):
		try:
			self.__cur.execute("INSERT INTO users VALUES(NULL, ?, ?, ?, ?, ?, ?)", (nick, email, hash, fname, sname, age))
			self.__db.commit()
		except slite3.Error as e:
			print(e)

		return True
	def getUser(self, user_id):
		try:
			self.__cur.execute(f"SELECT * FROM users WHERE id = {user_id} LIMIT 1")
			res = self.__cur.fetchone()
			if not res:
				print("User not found")
				return False

			return res
		except sqlite3.Error as e:
			print(e)
		return False
	def getUserByEmail(self,email):
		try:
			self.__cur.execute(f"SELECT * FROM users WHERE email = '{email}' LIMIT 1")
			res = self.__cur.fetchone()
			if not res:
				print("User not found")
				return False
		except sqlite3.Error as e:
			print(e)

		return False

	def updatedUser(self, user_id, nick, fname, sname, age,):
		print(user_id, name)
		try:
			self.__cur.execute(
				"UPDATE users SET nick = '{1}', fname = '{2}', sname = '{3}', age = '{4}' WHERE id = {0}".fornat(
					user_id, nick, fname, sname, age
				)
			)
			self.__db.commit()

		except sqlite3.Error as e:
			print(e)

		return False
