import random
import tkinter as tk
from words import word_list
from art import logo, stages

# Global variables for game state
chosen_word = ""
word_length = 0
display = []
lives = 6
end_of_game = False

# Function to start the game
def start_game():
    global chosen_word, word_length, display, lives, end_of_game
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    display = ["_"] * word_length
    lives = 6
    end_of_game = False
    update_display()
    guess_entry.config(state='normal')
    guess_button.config(state='normal')
    message_label.config(text="Guess a letter:", fg='blue')

# Function to handle guesses
def guess_letter():
    global lives, end_of_game
    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)

    if guess in display:
        message_label.config(text=f"You've already guessed {guess}", fg='orange')
        return

    if guess.lower() in chosen_word.lower():
        message_label.config(text=f"You guessed {guess}, that's in the word. ", fg='green')
        for position in range(word_length):
            letter = chosen_word[position]
            if letter.lower() == guess.lower():
                display[position] = letter
    else:
        message_label.config(text=f"You guessed {guess}, that's not in the word. You lose a life.", fg='red')
        lives -= 1
        if lives == 0:
            end_of_game = True
            message_label.config(text="You lose. The word was: " + chosen_word, fg='red')
            guess_entry.config(state='disabled')
            guess_button.config(state='disabled')

    update_display()

    if "_" not in display:
        end_of_game = True
        message_label.config(text="You win!", fg='green', font=("Courier", 40))
        guess_entry.config(state='disabled')
        guess_button.config(state='disabled')

def update_display():
    word_label.config(text=" ".join(display))
    hangman_label.config(text=stages[lives])

# Set up the main window
root = tk.Tk()
root.title("Hangman Game")
root.geometry("1000x1000")
root.configure(bg='lightblue')

# Display logo
logo_label = tk.Label(root, text=logo, font=("Courier", 25), justify="center", bg='lightblue', fg='black')
logo_label.pack()

# Word display
word_label = tk.Label(root, font=("Courier", 24), bg='lightblue', fg='black')
word_label.pack()

# Hangman stages display
hangman_label = tk.Label(root, text=stages[6], font=("Courier", 25), bg='lightblue', fg='brown')
hangman_label.pack()

# Message label
message_label = tk.Label(root, text="Guess a letter:", font=("Courier", 20), bg='lightblue', fg='blue')
message_label.pack()

# Entry field for guesses
guess_entry = tk.Entry(root, font=("Courier", 14), bg='white', fg='black')
guess_entry.pack()

# Guess button
guess_button = tk.Button(root, text="Guess", command=guess_letter, font=("Courier", 20), bg='yellow', fg='black')
guess_button.pack()

# Start button
start_button = tk.Button(root, text="Start Game", command=start_game, font=("Courier", 20), bg='green', fg='green')
start_button.pack()
#Exit button
exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Courier", 20), bg='red', fg='red')
exit_button.pack()


start_game()
root.mainloop()
