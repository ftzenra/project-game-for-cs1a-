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

# pang reset so everytime mag laro di same value
def reset_game():
    health = 3
    hints = 1
    word_pass = 0
    score = 0
    revealed_count = 0
    # pang reload to ng randomizer para di same value pag nag loop ung laro
    importlib.reload(randomizer)
# eto func ko pang clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
#rulesss
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
   

    print("Unscramble the letters to form a word.")
    print("You have 3 health points and gain rewards for correct answers.")
    print("rewards can be,health,hints,or points, level pass")
#welcome dialogues
def welcome():
    print("Welcome to the Word Scramble Game!")
    print("Try to unscramble the words and earn points.")
#pang show ng qoutes
def show_quotes():
    print(f"here quote you created{ randomizer.quote()}")
# pang check if na return na 4 word value
def cheacker():
    return all(correct_words)
# eto current na na letter sa scrambled, gamit to sa hint para mabigay mga letters
def current():
    return randomizer.scrambled_words[current_index]