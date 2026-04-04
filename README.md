# 🧠 Propositional Logic Quiz Game

Final project for **Discrete Mathematics 2**. 
This is a Python-based educational game that help students learn **propositional logic** through an interactive quiz format.

## 📘 What is Propositional Logic?

Propositional logic is a branch of logic that deals with **propositions**—statements that can be either **true** or **false**. It uses logical connectives to combine simple propositions into compound propositions:

- **Negation (~)**: NOT
- **Conjunction (^)**: AND  
- **Disjunction (v)**: OR
- **Implication (->)**: IF...THEN
- **Biconditional (<>)**: IF AND ONLY IF

A compound proposition can be classified as:

- **Tautology**: Always true (true for all truth value combinations)
- **Contradiction**: Always false (false for all truth value combinations)
- **Contingency**: Can be either true or false (depends on truth values)

This program generates **truth tables** to evaluate compound propositions and classify them accordingly.

## 🎮 Features

- 🧩 Interactive quiz-based gameplay (**5 rounds per session**)  
- 🎯 Two game modes:
  - **Expression Mode** — Solve logical expressions like `(p ^ q) v r`
  - **Statement Mode** — Solve real-world statements like  
    `"I will have coffee or I will have tea"`
- 🪜 Three difficulty levels:
  - Easy  
  - Medium  
  - Hard  
- 🏆 Dynamic scoring system with bonus points for harder levels  
- 📊 Automatic truth table generation with step-by-step evaluation  
- 🥇 Leaderboard system to track high scores  
- 🔗 Supports all logical connectives: `^`, `v`, `~`, `->`, `<>`  
- 🧠 Automatic classification of propositions:
  - Tautology  
  - Contradiction  
  - Contingency  

## 🧪 Example expressions

Some example expressions used in game:

- `(p ^ q) -> r`
- `(p ^ q) -> (r ^ s)`
- `~(p ^ ~q)`
- `r <> (p v q)`
- `(~p ^ ~q) -> (r v s)`

## ▶️ How to Run

```bash
python main.py
```

### 📦 Requirements
- Python 3.6+

### 🎮 Game Controls
1. Enter your name for the leaderboard
2. Choose a gamemode:
    * `1` = Expression Mode 
    * `2` = Statement)
3. Choose difficulty (1 = Easy, 2 = Medium, 3 = Hard)
    * `1` = Easy
    * `2` = Medium
    * `3` = Hard
4. For each question, input:
    * `a` = Contingency
    * `b` = Contradiction  
    * `c` = Tautology
5. Confirm your final answer using:
    * `y` = Submit answer

## 🗂️ Project Structure

```
propositional-logic/
├── main.py                 # Entry point
├── PropositionalLogic.py   # Core logic engine (truth tables, evaluation)
├── Game.py                 # Game loop and user interaction
├── JsonParser.py           # JSON data parsing and leaderboard management
├── Colors.py               # ANSI color formatting
├── dataset.json            # Question bank with statements and expressions
├── leaderboard.json        # Persistent score storage
└── README.md               # This file
```

## 🚀 Future Improvements

- 📂 Custom File Input
    - Allow users to load custom propositions from external files.
- ✅ Truth Value Validation
    - Add functionality to verify truth values by comparing them with generated truth tables.
