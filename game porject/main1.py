import random
import randomizer
import Datamodule
import utility

def show_quotes():
    print(f"here quote you created\n{randomizer.quote}")
   
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
while True:
    utility.welcome()
    print("\n1. Start Game\n2. View Rules\n3. Exit")
    choice = input("Enter your choice: ")


    if choice == "1":
        utility.clear_screen()
        utility.reset_game()
        while utility.health > 0 and not utility.cheacker():
            print(f"Health: {utility.health} | Score: {utility.score} | Hints: {utility.hints}")
            print(f"Progress: Word {utility.current_index + 1}/4")
            print("-" * 40)
            current_scrambled = randomizer.scrambled_words[utility.current_index]
            print(f"Unscramble this word: {current_scrambled}")
            
            game1 = input("Your answer: ").lower().strip()
            correct_word = randomizer.words[utility.current_index].lower()
            if game1 == correct_word:
                print("Correct!")
                utility.correct_words[utility.current_index] = True
                utility.score += 1
                print(f"Score: {utility.score}")
                print("\npress any key to go back")
                back_choice = input()
                utility.current_index += 1

                if utility.cheacker():
                    utility.clear_screen()
                    print("You Won!")
                    print()
                    show_quotes()
                    print("\nPress Enter to return to main menu")
                    input()
                    utility.clear_screen()
                    break
                else:
                    print(f"\nNext word coming up...")
                    input("Press Enter to continue")
                    utility.clear_screen()
                

            else:
                print("Wrong!")
                utility.health -= 1
                print(f"Health remaining: {utility.health}")


                if utility.health == 0:
                    print("Game Over!")
                    print("answer is ",correct_word)
                    print(f"final score: {utility.score}")
                    print("\npress any key to go back")
                    input()
                    utility.clear_screen()
                    break
                
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
                
    elif choice == "2":
        utility.clear_screen()
        utility.rules()
        print("\nPress Enter to go back")
        input()
        utility.clear_screen()
        
    elif choice == "3":
        print("Thanks for playing!")
        break