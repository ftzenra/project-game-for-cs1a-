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
    print("Game Rules:\n")
    print('''You have 3 health points and 1 Hint!
Unscramble the letters to form a word and gain rewards for each correct answer!
Rewards can be health, hints, points, or level pass.''')

def welcome():
    print("Welcome to Word Scramble Game!")
    print("Unscramble the words to earn points and rewards!")

def show_quotes():
    print(f"here is the quote you created: { randomizer.quote()}")
   

def cheacker():
    return all(correct_words)

def current():
    return randomizer.scrambled_words[current_index]