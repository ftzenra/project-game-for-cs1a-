import randomizer
import random
import Datamodule
import utility

while utility.health > 0:
    game1 = input(f"1. unscramble {randomizer.w1}: ")
    
    if game1 == randomizer.words[0]:
        print("Correct!")
        utility.score += 1
        break
        
    else:
        print("Wrong!")
        utility.health -= 1
        
        if utility.health == 0:
            print("Game Over!")
            break
        
        print("Want to use a hint? (y/n)")
        hint_choice = input()
        
        if hint_choice == "y" and utility.hints > 0:
            utility.hints -= 1
            print(f"{utility.hints} hints left.\n")
            utility.revealed_count += 1
            hint_display = list("_" * len(randomizer.words[0]))
            for i in range(utility.revealed_count):
                if i < len(randomizer.words[0]):
                    hint_display[i] = randomizer.words[0][i]
            print("Hint: " + ' '.join(hint_display))
        else:
            print("You don't have any hints left or you chose not to use a hint.\n")