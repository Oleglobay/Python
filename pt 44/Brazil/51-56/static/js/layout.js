$(document).ready(function() {
	var socket = io.connect();

	socket.on('connect', function() {
		console.log(window.location.pathname)
		socket.emit('my_eve', {data: window.location.pathname})
	})

	socket.on('sendNews', function(data) {
		console.log(data)
		for (const element of data){
			genCardHome(JSON.parse(element))
		}
	});

	socket.on('sendContact', function(data) {
		console.log(data)
		for (const element of data){
			getAccordion(JSON.parse(element))
		}
	});
});


function genCardHome(dataCards) {
	console.log(dataCards);
	var element = document.getElementById('home_card_block');
	var aLink = document.createElement("a");
	aLink.href = "/news/" + dataCards["id"];
	aLink.target = "_self"

	var card = document.createElement('div');
	card.className = "card";
	card.style.width = "18rem";

	var imageCard = document.createElement("img");
	imageCard.className = 'card-img-top';
	imageCard.src = dataCards["image"];

	var cardBody = document.createElement('div');
	cardBody.className = "card-body";

	var cardTitle = document.createElement("h5");
	cardTitle.className = "card-title";
	cardTitle.innerText = dataCards["title"];

	var cardText = document.createElement('p');
	cardText.className = "card-text";
	cardText.innerText = dataCards["description"];

	cardBody.appendChild(cardTitle);
	cardBody.appendChild(cardText);

	card.appendChild(imageCard);
	card.appendChild(cardBody);

	aLink.appendChild(card);

	element.appendChild(aLink);
};	
function getAccordion(dataCards) {
	var element = document.getElementById('accordion');
	var card = document.createElement('div');
	card.className = "card";

	var cardHead = document.createElement('div');
	cardHead.className = "card-header";
	cardHead.id = "heading"+dataCards["num"];

	var cardH5 = document.createElement('h5');
	cardH5.className = "mb-0";

	var cardButton = document.createElement('button');
	cardButton.className = "btn btn-link";
	cardButton.setAttribute('data-toggle',"collapse");
	cardButton.setAttribute('data-target',"#collapse"+dataCards["num"]);
	if (dataCards["num"] == "One") {
		cardButton.setAttribute('aria-expanded',"true");
	} else {
		cardButton.setAttribute('aria-expanded',"false");
	}
	cardButton.setAttribute('aria-controls',"collapse"+dataCards["num"]);

	var cardBT = document.createElement('p')
	cardBT.innerText = dataCards["title"]

	var cardDiv = document.createElement('div');
	cardDiv.id = "collapse"+dataCards["num"];
	cardDiv.className = "collapse";
	cardDiv.setAttribute('aria-labelledby',"heading"+dataCards["num"]);
	cardDiv.setAttribute('data-parent', "#accordion");

	var cardBody = document.createElement('div');
	cardBody.className = "card-body";

	var cardText = document.createElement('p');
	cardText.className = "card-text";
	cardText.innerText = dataCards["description"];

	cardBody.appendChild(cardText);
	cardDiv.appendChild(cardBody);

	cardButton.appendChild(cardBT)
	cardH5.appendChild(cardButton);
	cardHead.appendChild(cardH5);

	cardBody.appendChild(cardText);
	cardDiv.appendChild(cardBody);

	card.appendChild(cardHead);
	card.appendChild(cardDiv);

	element.appendChild(card);
}