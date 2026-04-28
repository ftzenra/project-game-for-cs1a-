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
mode1_score = 0
mode2_score = 0
mode3_score = 0

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
    print("======================== GAME RULES ========================\n")
    print('''        
Unscramble the letters to form a word and gain rewards for 
each correct answer!

Rewards can be \033[32mhealth\033[0m, \033[33mhints\033[0m, or even \033[35mlevel pass\033[0m!\n''')
    print("="*60)

#infinite mode
def rules_mode1():
    print("="*60)
    print('''        
    MODE 1: \033[34mInfinity and Beyond! ∞\033[0m

    Player has: \033[31m3HP\033[0m, \033[33m1 Hint\033[0m, and \033[35m0 Word Pass\033[0m
                    
          \033[36mUnscramble words, and for every 5 correct words, 
    your level increases and so does the word length until 
    you reach the 10-letter words!\033[0m\n''') 
    print("="*60)  

#quote builder mode
def rules_mode2():
    print("="*60)
    print('''        
    MODE 2: \033[34mComplete the Quote!\033[0m

    Player has: \033[31m3HP\033[0m, \033[33m1 Hint\033[0m, and \033[35m0 Word Pass\033[0m

          \033[36mUnscramble 4 words to complete a quote that'll 
    insipre you!\033[0m\n''')
    print("="*60)

#extreme mode
def rules_mode3():
    print("="*60)  
    print('''        
    MODE 3: \033[34mExtremers Challenge!\033[0m

    Player has: \033[31m3HP\033[0m, \033[33m1 Hint\033[0m, and \033[35m1 Word Pass\033[0m
          
          \033[36mUnscramble deep words with at least 10-letters 
    to challenge your vocabulary!\033[0m\n''')
    print("="*60)

#welcome dialogues
def welcome():
    print("""\033[36m _    _      _                             _          _   _                   
| |  | |    | |                           | |        | | | |                  
| |  | | ___| | ___ ___  _ __ ___   ___   | |_ ___   | |_| |__   ___          
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \  | __/ _ \  | __| '_ \ / _ \         
\  /\  /  __/ | (_| (_) | | | | | |  __/  | || (_) | | |_| | | |  __/         
 \/  \/ \___|_|\___\___/|_| |_| |_|\___|   \__\___/   \__|_| |_|\___|         
                                                                              
                                                                              
 _____                          _     _        _____                         \033[31m_\033[0m  
\033[36m/  ___|                        | |   | |      |  __ \                     \033[0m  \033[31m| |\033[0m 
\033[36m\ `--.  ___ _ __ __ _ _ __ ___ | |__ | | ___  | |  \/ __ _ _ __ ___   ___ \033[0m  \033[31m| |\033[0m 
\033[36m `--. \/ __| '__/ _` | '_ ` _ \| '_ \| |/ _ \ | | __ / _` | '_ ` _ \ / _ \ \033[0m \033[31m| |\033[0m 
\033[36m/\__/ / (__| | | (_| | | | | | | |_) | |  __/ | |_\ \ (_| | | | | | |  __/\033[0m  \033[31m|_|\033[0m 
\033[36m\____/ \___|_|  \__,_|_| |_| |_|_.__/|_|\___|  \____/\__,_|_| |_| |_|\___|\033[0m  \033[31m(_)\033[0m 
                                                                              
                                                                              """)
    print('''created by: \033[34mGROUP 7\033[0m
            \033[34mCamantigue, Paul Arcee\033[0m
            \033[34mCaole, Krisha Nicole\033[0m
            \033[34mDarm, Maria Jonel\033[0m
            \033[34mMonteflacon, Jake Andrei\033[0m
            \033[34mPimentel, Margareth Ysabel Louise\033[0m''')

#pang show ng quotes
def show_quotes():
    print(f"here is the quote you created: { randomizer.quote()}")

# pang check if na return na 4 word value
def cheacker():
    return all(correct_words)

# eto current na letter sa scrambled, gamit to sa hint para mabigay mga letters
def current():
    return randomizer.scrambled_words[current_index]