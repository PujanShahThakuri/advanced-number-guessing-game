# advanced-number-guessing-game
A simple Python game where you guess a random number with input validation and game history logging.
# 🎯 Advanced Number Guessing Game

A simple yet enhanced Python number guessing game with:

- 🎯 Random number generation
- ✅ Input validation
- 📈 Hints for guesses (too high/low)
- 💾 Game history logging with timestamp
- 🔁 Replay option

## 📌 How It Works

- The program randomly chooses a number between 1 and 100.
- The player has 7 attempts to guess the number.
- After each guess, the player receives feedback:
  - `📉 Too low!`  
  - `📈 Too high!`
- Win or lose, each game’s result is saved to a file called `game_history.txt`.

## 📂 Files Included

- `guessing_game.py`: Main Python file with the full game logic.
- `README.md`: This file.
- `game_history.txt`: Generated automatically after the first play to store results.

## 🛠️ How to Run

Make sure you have Python installed.

```bash
python guessing_game.py

