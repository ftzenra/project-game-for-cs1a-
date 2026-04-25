import random
import randomizer
import Datamodule
import utility

# eto sir para sa qoutes
def show_quotes():
    print(f"here quote you created\n{randomizer.quote}")

# eto process ng hints
def hint():
    utility.hints -= 1
    print(f"{utility.hints} hints left.\n")
    utility.revealed_count += 1
    hint_display = list("_" * len(randomizer.words[utility.current_index]))
    for i in range(utility.revealed_count):
        if i < len(randomizer.words[utility.current_index]):
            hint_display[i] = randomizer.words[utility.current_index][i]
    print("Hint: " + ' '.join(hint_display))
utility.clear_screen()

# eto main process ng game
while True:
    utility.welcome()
    print("\n1. Start Game\n2. View Rules\n3. Exit")
    choice = input("Enter your choice: ")
#eto ung choice 1 para sa start ng game
    if choice == "1":
        utility.clear_screen()
        # pang reset ng randomizer 
        utility.reset_game()
        # main interface pag nasa game na
        while utility.health > 0 and not utility.cheacker():
            print(f"Health: {utility.health} | Score: {utility.score} | Hints: {utility.hints}")
            print(f"Progress: Word {utility.current_index + 1}/4")
            print("-" * 40)
            current_scrambled = randomizer.scrambled_words[utility.current_index]
            print(f"Unscramble this word: {current_scrambled}")
            
            game1 = input("Your answer: ").lower().strip()
            correct_word = randomizer.words[utility.current_index].lower()
            # eto ung pag tama sagot nya
            if game1 == correct_word:
                print("Correct!")
                utility.correct_words[utility.current_index] = True
                utility.score += 1
                randomizer.gifts()
                print(f"Score: {utility.score}")
                # random reward every manalo pero may chances dipende gano ka rare reward
                print(f"You a random gift; {randomizer.reward_type}= +1")
                print("\npress any key to go back")
                back_choice = input()
                utility.current_index += 1
                # pang return ng correct na word para malaman if na complete mona 4 na word pang buo ng qoutes
                if utility.cheacker():
                    utility.clear_screen()
                    print("You Won!")
                    print()
                    show_quotes()
                    print("\nPress Enter to return to main menu")
                    input()
                    utility.clear_screen()
                    break
                # eto pag dipa buo ung checker sa taas need mopa ma complte 4 na word
                else:
                    print(f"\nNext word coming up...")
                    input("Press Enter to continue")
                    utility.clear_screen()
                
            #pag mali lang to
            else:
                print("Wrong!")
                utility.health -= 1
                print(f"Health remaining: {utility.health}")

                # eto game over if wala na health
                if utility.health == 0:
                    print("Game Over!")
                    print("answer is ",correct_word)
                    print(f"final score: {utility.score}")
                    print("\npress any key to go back")
                    input()
                    utility.clear_screen()
                    break
                # ask player if want hint
                print(f"Want to use a hint? (y/n) -{utility.hints}hint available"  )
                hint_choice = input().lower()
                if hint_choice=="y" and utility.hints > 0:
                    utility.clear_screen()
                    hint()
                elif hint_choice == "n":
                    utility.clear_screen()
                    print("====did not use hint===")
                elif utility.hints <= 0:
                    utility.clear_screen()
                    print("===0 hints===")
                else:
                    print("===wrong input===")
                print(f"want to use word pass?")
                pass_choice= input().lower()
                # ask sa player if want ng word pass
                if pass_choice == "y" and utility.word_pass > 0:
                    utility.clear_screen()
                    print(f"the word is { randomizer.words[utility.current_index].lower()}")
                else:
                    pass
    # wala to parang sa rules
    elif choice == "2":
        utility.clear_screen()
        utility.rules()
        print("\nPress Enter to go back")
        input()
        utility.clear_screen()
    # pang exit para masaya
    elif choice == "3":
        print("Thanks for playing!")
        break