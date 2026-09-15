 var socket = io();
 socket.on('connect', function(){
	 socket.emit('my event', {data: 'connected'});
 });



function genCardHome(dataCards) {
debugger
var elemet = document.getElementById("home_card_block");
var aLink = document.createElement("a")
aLink.href = "/news/" + dataCards.id;
alink.terget = "_self"

var card = document.createElement("div");
card.className = "card";
card.style.width = "18rem";

var imageCard = document.createElement("img");
imageCard.className = "card-img-top";
imageCard.scr = dataCards.image;

var cardBody = document.createElement("div")
cardBody.className = "card-body";

var cardTitle = document.createElement("h5");
cardTitle.className = "card-title";
cardTitle.innerText = dataCards.title;

var cardText = document.createElement("p");
cardText.className = "card-text";
cardText.innerText = dataCards.description;

cardBody.appendChild(cardTitle);
cardBody.appendChild(cardText);

card.appendChild(imageCard);
card.appendChild(cardBody);

aLink.appendChild(card);

element.appendChild(alink);
}



app.config['secred_key'] = 'secret!'
socketio = SocketIO(app)

login_manager = loginManager(app)


class Person:

  def __init__(self, againUsername, intAgainPassword, email, age, aqqintAgainPassword, hobby = "I DONT HAE HOHBY"):
    self.againUsername = againUsername
    self.intAgainPassword =  intAgainPassword
    self.email = email
    self.age = age
    self.aqqintAgainPassword = aqqintAgainPassword
    self.hobby = hobby

  def speak(self, word):
    return self.againUsername + " says " + word

  def updateAge(self, age):
    self.age  = age

  def getAge(self):
   return self.age

  def getName(self):
   return self.againUsername

class News:
    def __init__(self, image, title, description):
        self.image = image
        self.title = title
        self.description = description
