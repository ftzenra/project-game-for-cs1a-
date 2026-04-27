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
    global health, hints, word_pass, score, revealed_count
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

#rules
def rules():
    print("======================== GAME RULES =========================\n")
    print('''        
Unscramble the letters to form a word and gain rewards for 
each correct answer!

Rewards can be health, hints, or even level pass!''')
    print("\n\n=======================================================\n")

def rules_mode1():
    print("="*60)
    print('''        
    MODE 1: Infinity and Beyond! ∞

    Player has: 3HP, 1 Hint, and 0 Word Pass
                    
    Unscramble words, and for every 5 correct words, your level 
    increases and so does the word length until you reach the 
    10-letter words.\n''') 
    print("="*60)      
def rules_mode2():
    print("="*60)
    print('''        
    MODE 2: Complete the Quote! 

    Player has: 3HP, 1 Hint, and 0 Word Passes

    Unscramble 4 words to complete a quote that'll insipre you!\n''')
    print("="*60)

def rules_mode3():
    print("="*60)  
    print('''        
    MODE 3: Extremers Challenge!

    Player has: 3HP, 1 Hint, and 1 Word Pass
          
    Unscramble deep words with at least 10-letters to challenge
    your vocabulary!\n''')
    print("="*60)

#welcome dialogues
def welcome():
    print("Welcome to The Word Scramble Game!")
    print("created by: BSCS-1A")

#pang show ng quotes
def show_quotes():
    print(f"here is the quote you created: { randomizer.quote()}")

# pang check if na return na 4 word value
def cheacker():
    return all(correct_words)

# eto current na letter sa scrambled, gamit to sa hint para mabigay mga letters
def current():
    return randomizer.scrambled_words[current_index]