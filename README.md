
# 🎮 Hangman Game – Terminal-Based Word Guessing Game

A terminal-based Hangman game written in Python that lets players guess randomly chosen words within limited attempts. The project features a user-friendly interface, scoring system, and an administrator mode to manage the word bank and high scores.

---

## 📘 Project Information

- **Project Title**: Hangman Game
- **Course**: CS-115 – Computer Programming
- **University**: NED University of Engineering and Technology
- **Semester**: Fall 2022
- **Type**: Term Project
- **Group Members**:
  - Muhammad Zunain (CS-0086) – Admin Mode
  - Muhammad Zuhaib Noor (CS-0081) – Player Mode
  - Muhammad Owais (CS-0080) – Game Logic

---

## 🎯 Objective

The game mimics the classic hangman experience through a CLI. It consists of two primary modes:

- **Player Mode**: Guess the secret word, view game rules, see scores.
- **Admin Mode**: Add new words, reset high scores, and manage word lists.

---

## 🔐 Admin Features

- Add words to the `word.txt` dictionary
- Reset the highest score and player's name
- View scores of all previous players

---

## 🕹️ Gameplay Mechanics

- Player starts with **6 guesses** and **3 warnings**
- Secret word is randomly selected from `word.txt` (55,000+ words)
- Each round, the player:
  - Is shown available letters
  - Guesses one letter at a time
  - Gets immediate feedback
- Game ends when the player either:
  - Guesses the word correctly
  - Runs out of guesses

### ⚠️ Rules Summary

-  Correct guesses reveal letters
-  Incorrect vowels cost 2 guesses
-  Incorrect consonants cost 1 guess
-  Invalid or repeated input reduces warnings (then guesses)
-  Score = Remaining guesses × Unique letters in the word
-  If score > previous high, player is congratulated

---
---

## 🛠 Technologies Used

- **Python 3**
- `os.system('cls')` for screen clearing
- File handling with `.txt` files
- Custom CLI interface using print/input
- No external libraries

---

## 💻 Getting Started

### Run Locally

```python
git clone https://github.com/yourusername/hangman-game.git
cd hangman-game
python RUN.py
```


# 📸 Screen Shot

![h1](https://github.com/Muhammad-Zunain/Hangman-Game/assets/146370860/8be267af-0e22-4c8a-af32-816478d6ec68)

## 🤝 Contributors
- [**Muhammad Zunain**](https://github.com/Muhammad-Zunain)
- [**Muhammad Owais**](https://github.com/MuhammadOwais03)
- **Zuhaib Noor**


