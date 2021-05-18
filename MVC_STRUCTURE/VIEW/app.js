const submitButton = document.getElementById('submitButton');
const chatbotInput = document.getElementById('chatbotInput');
const chatbotOutput = document.getElementById('chatbotOutput');

submitButton.onclick = userSubmitEventHandler;
chatbotInput.onkeyup = userSubmitEventHandler;

function userSubmitEventHandler(event) {
    if (
        (event.keyCode && event.keyCode === 13) ||
        event.type === 'click'
    ) {
        //chatbotOutput.innerText = 'thinking...';
        console.log(chatbotInput.value);
        var s1='Me: ';
        var s2=s1.concat(chatbotInput.value);
        var tag = document.createElement("p");
        var text = document.createTextNode(s2);
        tag.appendChild(text);
        var element = document.getElementById("chatWindow");
        element.appendChild(tag);
        window.scrollTo(300, 500);
        askChatBot(chatbotInput.value);
    }
}

function askChatBot(userInput) {
    const myRequest = new Request('/', {
        method: 'POST',
        body: userInput
    });

    fetch(myRequest).then(function(response) {
        if (!response.ok) {
            throw new Error('HTTP error, status = ' + response.status);
        } else {
            return response.text();
        }
    }).then(function(text) {
        var tag = document.createElement("p");
        var text = document.createTextNode(text);
        tag.appendChild(text);
        var element = document.getElementById("chatWindow");
        element.appendChild(tag);
        chatbotInput.value = '';
        //chatbotOutput.innerText = text;
    }).catch((err) => {
        console.error(err);
    });
}
