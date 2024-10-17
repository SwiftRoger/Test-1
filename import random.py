import random
import tkinter as tk

def guessing_game():
    global number_to_guess, attempts

    # Generate a random number between 1 and 50
    number_to_guess = random.randint(1, 50)
    attempts = 0

    # Update the label with the welcome message
    welcome_label.config(text="Welcome to the Guessing Game!\nI have selected a number between 1 and 50. Try to guess it!")

    # Enable the guess entry and button
    guess_entry.config(state="normal")
    guess_button.config(state="normal")
    guess_entry.delete(0, tk.END)  # Clear the entry field

def check_guess():
    global attempts

    # Get user input
    try:
        user_guess = int(guess_entry.get())
    except ValueError:
        result_label.config(text="Please enter a valid number.")
        return

    attempts += 1

    # Check the guess
    if user_guess > number_to_guess:
        result_label.config(text="Your guess is too high.")
    elif user_guess < number_to_guess:
        result_label.config(text="Your guess is too low.")
    else:
        result_label.config(text=f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        guess_entry.config(state="disabled")
        guess_button.config(state="disabled")

# Create the main window
window = tk.Tk()
window.title("Guessing Game")

# Create welcome label
welcome_label = tk.Label(window, text="", font=("Arial", 16))
welcome_label.pack(pady=20)

# Create guess entry
guess_entry = tk.Entry(window, width=10, state="disabled")
guess_entry.pack()

# Create guess button
guess_button = tk.Button(window, text="Guess", command=check_guess, state="disabled")
guess_button.pack(pady=10)

# Create result label
result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack()

# Start the game
guessing_game()

# Run the main loop
window.mainloop()