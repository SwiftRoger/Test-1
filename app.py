from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

@app.route('/')
def home():
    session['number_to_guess'] = random.randint(1, 50)
    session['attempts'] = 0
    return render_template('index.html', message="Welcome to the Guessing Game! Guess a number between 1 and 50.")

@app.route('/guess', methods=['POST'])
def guess():
    user_guess = request.form['guess']
    if not user_guess.isdigit():
        return render_template('index.html', message="Please enter a valid number.")
    
    user_guess = int(user_guess)
    session['attempts'] += 1
    number_to_guess = session['number_to_guess']

    if user_guess > number_to_guess:
        message = "Your guess is too high."
    elif user_guess < number_to_guess:
        message = "Your guess is too low."
    else:
        message = f"Congratulations! You've guessed the number {number_to_guess} in {session['attempts']} attempts."
        message += " Want to try again?"
        return render_template('index.html', message=message, show_try_again=True)

    return render_template('index.html', message=message)

@app.route('/try-again')
def try_again():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)