

# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a classic Hangman game in Python. Practice string manipulation, loops, conditionals, and random selection by creating a word-guessing game where players try to reveal a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Hangman Game Logic

#### Description
Create the main game loop for Hangman. The program should randomly select a word, accept letter guesses, and display the current progress. Track incorrect guesses and end the game with a win or lose message.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Accept letter guesses from the player
- Show current progress using underscores for unguessed letters (e.g., _ a _ _ m a n)
- Track and display the number of incorrect guesses remaining
- End when the word is fully guessed or attempts are exhausted
- Display a win or lose message

Example:
```
Word: _ a _ _ m a n
Guesses left: 4
Guessed letters: a, m, n, h
Enter your guess: g
```

### 🛠️ Word List & Replay Feature

#### Description
Add a list of at least 10 words for the game to choose from. Implement a feature that allows the player to play again after each round.

#### Requirements
Completed program should:

- Use a list of at least 10 possible words
- Allow the player to replay the game after finishing
- Reset all game variables for each new round
