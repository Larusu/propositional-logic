import sys
import time
import random
from Colors import Colors
from JsonParser import JsonParser
from PropositionalLogic import PropositionalLogic

class Game:
    def __init__(self):
        self.color = Colors() 
        
        try:
            self.json = JsonParser()
        except FileNotFoundError:
            print(self.color.error("Data doesn't exist. Closing program."))
            return
        except json.JSONDecodeError:
            print(self.color.error("dataset.json is corrupted. Closing program."))
            return

        self.MAX_ROUND = 5
        self.ids = []
        self.score = 0
        self.gamemode = "statement"
        
    def run(self):
        self._initializeGame()

        currentRound = 0
        while currentRound < self.MAX_ROUND:
            print(self.color.yellowAndUnderlined(f"Round {currentRound + 1}") 
                  + " | " + 
                  self.color.lightGreen(f"Score: {self.score}"))
            self._startGame(currentRound)
            currentRound += 1
        
        self.json.storeLeaderboard(self.name, self.score)
        print('\n' + self.color.success("Congratulations! Thank you for playing :) "))
        print(self.json.showLeaderboard())
        

    def _startGame(self, currentRound : int):
        # get random id
        id = random.choice(self.ids)

        # initializes variables and instantiate class
        statement, expression = self.json.getStatementAndLogic(id)
        question = expression if self.gamemode == "expression" else statement
        logic = PropositionalLogic(expression)
        
        # to prevent crash when question is fewer than MAX_ROUNDS
        if currentRound == 0:
            self.MAX_ROUND = min(
                self.MAX_ROUND,
                self.json.getDataSizeByDifficulty(self.difficulty)
            )
        print(f"{currentRound + 1}. {self.color.bold(question)}")

        # user input
        correctAnswer = logic.evaluateClassification()
        userAnswer = ""
        while True:
            userAnswer = input(": ").strip().lower()
            if (userAnswer == 'a' or userAnswer == 'b' or userAnswer == 'c'):
                validation = input("final answer?(y/n): ").strip().lower()
                if validation != 'y':
                    continue
                print()
                break
        
        userClassification = ""
        match userAnswer:
            case 'a':
                userClassification = "Contingency"
            case 'b':
                userClassification = "Contradiction"
            case 'c':
                userClassification = "Tautology"
        
        print("The engine is thinking...")
        
        # print with animation
        truthTable = logic.getTruthTable()
        for char in truthTable:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.02)
        print()

        # check if answer is correct or not
        isCorrect = False
        if userClassification.casefold() == correctAnswer.casefold():
            self.score += self.point
            print(f"{self.color.success("Correct Answer!")}", end=" | ")
        else:
            print(f"{self.color.error("Wrong Answer.")}", end=" | ")
        print(correctAnswer) 

        # remove id so that it wont be called again
        self.ids.remove(id)

        print("\n ")
 
    def _initializeGame(self):
        print(self.color.bold(f"""                                                                              
=======================================================================================================
▄▄▄▄  ▄▄▄▄   ▄▄▄  ▄▄▄▄   ▄▄▄   ▄▄▄▄ ▄▄ ▄▄▄▄▄▄ ▄▄  ▄▄▄  ▄▄  ▄▄  ▄▄▄  ▄▄      ▄▄     ▄▄▄   ▄▄▄▄ ▄▄  ▄▄▄▄ 
██▄█▀ ██▄█▄ ██▀██ ██▄█▀ ██▀██ ███▄▄ ██   ██   ██ ██▀██ ███▄██ ██▀██ ██      ██    ██▀██ ██ ▄▄ ██ ██▀▀▀ 
██    ██ ██ ▀███▀ ██    ▀███▀ ▄▄██▀ ██   ██   ██ ▀███▀ ██ ▀██ ██▀██ ██▄▄▄   ██▄▄▄ ▀███▀ ▀███▀ ██ ▀████ 

=======================================================================================================

Direction:
    1. Identify if the given statement is contingency, contradiction, or tautology
    2. This is a pointing system game that lasts for 5 rounds.
    3. The game has 2 gamemodes with 3 difficulties.
        Gamemode: 
            1. Expression (p v q)
            2. Statement (I will have coffee or I will have tea)

               | Expression | Statement |
        Easy   |    1 pt    |    2 pt   |
        Medium |    2 pt    |    4 pt   |
        Hard   |    3 pt    |    6 pt   | {self.color.error("Note: Your points is save locally")}

        {self.json.showLeaderboard()}
                              """))
        # Name input
        while True:
            self.name = input("Input your name (for points): ").strip()
            if input("Are you sure? (y/n): ").strip().lower() == "y":
                break
        
        # Gamemode input
        inputMode = self.getUserInput("Choose gamemode (1 = expression, 2 = statement): ", 1, 2)
        
        # Difficulty input)
        inputDifficulty = self.getUserInput("Choose difficulty (1 = easy, 2 = medium, 3 = hard): ", 1, 3)

        if(inputMode == 1):
            self.gamemode = "expression"
        
        if inputDifficulty == 1:
            self.difficulty = "easy"
            self.point = 1 if self.gamemode == "expression" else 2 
        elif inputDifficulty == 2:
            self.difficulty = "medium"
            self.point = 2 if self.gamemode == "expression" else 4
        elif inputDifficulty == 3:
            self.difficulty = "hard"
            self.point = 3 if self.gamemode == "expression" else 6

        print("\n")
        difficultyCount = self.json.getIdsByDifficulty(self.difficulty)
        for d in difficultyCount:
            self.ids.append(d)

        print("Type only the letter of your answer. (case insensitive)\na = contingency\nb = contradiction\nc = tautology")

    def getUserInput(self, prompt: str, min_val: int = None, max_val: int = None) -> int:
        while True:
            try:
                value = int(input(prompt))
                if min_val is not None and max_val is not None:
                    if not (min_val <= value <= max_val):
                        print(f"Enter a number between {min_val} and {max_val}.")
                        continue
                confirm = input("Are you sure? (y/n): ").strip().lower()
                if confirm == "y":
                    return value
            except ValueError:
                print("Please enter a valid number.")
