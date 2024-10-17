let numberToGuess;
let attempts;

function guessingGame() {
    numberToGuess = Math.floor(Math.random() * 50) + 1;
    attempts = 0;

    document.getElementById('welcome-message').textContent = "Welcome to the Guessing Game! I have selected a number between 1 and 50. Try to guess it!";
    document.getElementById('guess-input').disabled = false;
    document.getElementById('guess-button').disabled = false;
    document.getElementById('guess-input').value = ''; // Clear the input
    document.getElementById('result').textContent = ''; // Clear previous results
    document.getElementById('try-again-button').style.display = 'none'; // Hide Try Again button
}

function checkGuess() {
    const userGuess = parseInt(document.getElementById('guess-input').value);
    attempts++;

    if (userGuess > numberToGuess) {
        document.getElementById('result').textContent = "Your guess is too high.";
    } else if (userGuess < numberToGuess) {
        document.getElementById('result').textContent = "Your guess is too low.";
    } else {
        document.getElementById('result').textContent = `Congratulations! You've guessed the number ${numberToGuess} in ${attempts} attempts.`;
        document.getElementById('guess-input').disabled = true;
        document.getElementById('guess-button').disabled = true;
        document.getElementById('try-again-button').style.display = 'inline'; // Show Try Again button
    }
}

// Event listeners
document.getElementById('guess-button').addEventListener('click', checkGuess);
document.getElementById('try-again-button').addEventListener('click', guessingGame);

// Start the game
guessingGame();