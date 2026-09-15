class Person:

	def __init__(self, fName, sName, nickname, email, password, age):
		self.fName = fName
		self.sName = sName
		self.nickname = nickname
		self.email = email
		self.password = password
		self.age = age

	def speak(self, word):
		return self.fName + " says " + word
	
	def update(self, fName, sName, nickname, email, age):
		self.fName = fName
		self.sName = sName
		self.nickname = nickname
		self.email = email
		self.age = age

	def getEmail(self):
		return self.email	

	def getName(self):
		return self.fName

	def getWord(self):
		return self.password

	def getNick(self):
		return self.nickname

	def getAge(self):
		return self.age	

	def getFN(self):
		return self.fName

	def getSN(self):
		return self.sName

	def getAll(self):
		return [self.fName, self.sName, self.nickname, self.email, self.password, self.age]
