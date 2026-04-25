import os
import randomizer
import random
import importlib
health = 3
hints = 1
word_pass = 0
score = 0
revealed_count = 0
current_index = 0
correct_words = [False, False, False, False]

def reset_game():
    """Reset all game variables for a new game"""
    health = 3
    hints = 1
    word_pass = 0
    score = 0
    revealed_count = 0
    importlib.reload(randomizer)
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def rules():
    print("Unscramble the letters to form a word.")
    print("You have 3 health points and gain rewards for correct answers.")
    print("rewards can be,health,hints,or points, level pass")

def welcome():
    print("Welcome to the Word Scramble Game!")
    print("Try to unscramble the words and earn points.")

def show_quotes():
    print(f"here quote you created{ randomizer.quote()}")
   

def cheacker():
    return all(correct_words)

def current():
    return randomizer.scrambled_words[current_index]
    