# Hangman Game

Welcome to the Hangman Game! This is a simple yet fun implementation of the classic Hangman game using Python and Tkinter for the graphical user interface (GUI). This project was developed as part of my Python Programming Internship at CodeAlpha.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Overview](#code-overview)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- Random word selection from a predefined list
- User-friendly graphical interface for guessing letters
- Visual representation of the hangman stages
- Real-time feedback on guesses
- Win/loss detection with appropriate messages

## Installation

To run the Hangman game on your local machine, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/hangman-game.git
    cd hangman-game
    ```

2. **Install the required dependencies:**
    Ensure you have Python installed on your machine. You can download it from [here](https://www.python.org/downloads/).

3. **Run the game:**
    ```bash
    python hangman.py
    ```

## Usage

Once you run the game, a GUI window will open with the Hangman game interface. Click on "Start Game" to begin playing. Guess the letters by typing them into the input field and clicking the "Guess" button. You have 6 lives to guess the word correctly. Good luck!

## Code Overview

- `hangman.py`: The main Python script that contains the game logic and GUI implementation.
- `words.py`: A separate module containing a list of words for the game.
- `art.py`: A module containing the hangman stages and logo ASCII art.

### Main Functions

- `start_game()`: Initializes the game state and starts a new game.
- `guess_letter()`: Handles the logic for guessing a letter and updating the game state.
- `update_display()`: Updates the GUI with the current game state.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgements

- Thanks to the CodeAlpha team for providing this learning opportunity.
- Special thanks to the creators of Python and Tkinter for making such great tools available to developers.

---
