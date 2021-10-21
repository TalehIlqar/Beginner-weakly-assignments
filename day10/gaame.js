var psychicLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];

var youWin = 0;

var youLose = 0;

var guessesLeft = 10;

var guessedLetters = [];

document.onkeyup = function (event) {
    var yourGuess = event.key;
    guessedLetters.push(yourGuess);
    var psychicAns = psychicLetters[Math.floor(Math.random() * psychicLetters.length)];

    if (yourGuess === psychicAns) {
        youWin++;
        guessesLeft = 10;
    }
    else {
        guessesLeft--;
    }
    if (guessesLeft === 0) {
        youLose++;
        guessesLeft = 10;
    }

var html = "<p>Guess what letter I'm thinking of:</p>" + "<p>Wins: " + youWin + "</p>" + "<p>Loses: " + youLose + "<p>Guesses Remaining: " + guessesLeft + "<p>Guessed Letter: " + guessedLetters.join(', '); //Show guessed letters here
document.querySelector("#psychicAct").innerHTML = html;
}


document.addEventListener('keydown', function(event){
    console.log(event.key)
document.getElementById('s').innerHTML += `${event.key}, `
})
