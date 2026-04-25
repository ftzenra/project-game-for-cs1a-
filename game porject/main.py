
import random
import randomizer
import Datamodule
import utility
import importlib

def hint():
    utility.hints -= 1
    print(f"{utility.hints} hints left.\n")
    utility.revealed_count += 1
    hint_display = list("_" * len(randomizer.words[0]))
    for i in range(utility.revealed_count):
        if i < len(randomizer.words[0]):
            hint_display[i] = randomizer.words[0][i]
    print("Hint: " + ' '.join(hint_display))
utility.clear_screen()
while True:
    utility.welcome()
    print("\n1. Start Game\n2. View Rules\n3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        utility.reset_game()
        while utility.health > 0:
            utility.clear_screen()
            print(f"Health: {utility.health} | Score: {utility.score} | Hints: {utility.hints}")
            print(f"\nUnscramble this word: {randomizer.w1}")
            
            game1 = input("Your answer: ")
            
            if game1.lower() == randomizer.words[0].lower():
                utility.score += 10  
                print(f"Score: {utility.score}")
                print("\nPress Enter to continue to next word...")
                input()
                importlib.reload(randomizer)
                utility.clear_screen()
                
            else:
                print("Wrong!")
                utility.health -= 1
                print(f"Health remaining: {utility.health}")
                
                if utility.health == 0:
                    print("\nGame Over!")
                    print(f"The correct answer was: {randomizer.words[0]}")
                    print(f"Final Score: {utility.score}")
                    print("\nPress Enter to return to main menu")
                    input()
                    utility.clear_screen()
                    break
                print(f"\nWant to use a hint? (y/n) - {utility.hints} hints available")
                hint_choice = input().lower()
                
                if hint_choice == "y" and utility.hints > 0:
                    utility.clear_screen()
                    hint()
                    input("Press Enter to continue...")
                    utility.clear_screen()
                elif hint_choice == "n":
                    utility.clear_screen()
                    print("No hint used.")
                elif utility.hints <= 0:
                    utility.clear_screen()
                    print("You have no hints left!")
                else:
                    utility.clear_screen()
                    print("Invalid input!")
        
    elif choice == "2":
        utility.clear_screen()
        utility.rules()
        print("\nPress Enter to go back")
        input()
        utility.clear_screen()
        
    elif choice == "3":
        print("Thanks for playing!")
        break