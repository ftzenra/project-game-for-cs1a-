import random
import randomizer
import Datamodule
import utility
import OOP

#classic play ginagamit neto classic dun OOP
def classic_play():
    """Playing Infinite mode with rising difficulty"""
    game = OOP.InfiniteMode()
    utility.clear_screen()

    print("="*40)
    print("INFINITE MODE")
    print("="*40)
    # condition para mag loop
    while not game.is_game_over() and not game.is_victory():
        utility.clear_screen()
        #kuha ng health saoop na galing naman sa utility
        print("=============INFINITE MODE=============")
        print(f"\nHealth: {game.health} |  Score: {game.score} |  Hints: {game.hints} |  Passes: {game.word_passes}\n")
        print(f"{game.get_mode_info()}\n")
        print("="*40)

        #istore ung scrable
        currentword=game.get_current_word()
        scrambled = game.scramble_word(currentword)
        print(f"UNSCRAMBLE: {scrambled}")
        
        answer = input("ANSWER: ").lower().strip()

        if game.check_answer(answer,currentword):
            print("\nCORRECT!\n")
            utility.score = game.score
            game.score +=1
            utility.mode1_score = max(utility.mode1_score, game.score)  # score tracking for high score
            reward = game.give_reward()

            # incase of level up
            level_up = game.next_word()
            if level_up:
                print({level_up})
                if "VICTORY" in level_up:
                    print(f"\nFINAL SCORE: {game.score} ")
                    input("\nPress Enter to continue...")
                    return
                input("Press Enter to continue...")
            else:
                print("\nPress any key to continue...")
                input()
        else:
            print("wrong answer")
            game.health -=1

            if game.is_game_over():
                utility.clear_screen()
                print(f"\nGAME OVER! Final Score: {game.score} ")
                print(f"The correct word was: {currentword}")
                print("\nPress any key to go back...")
                input()
                return
            utility.clear_screen()
            print(f"\nWant to use a hint? (y/n) - {game.hints} hints available")
            hint_choice = input("> ").lower().strip()
            if hint_choice == "y" and game.hints> 0:
                utility.clear_screen()
                hint = game.show_hint(currentword)
                if hint:
                    print(f"UNSCRAMBLE: {scrambled}")
                    print(f"🔍 Hint: {hint}")
            elif game.hints <= 0:
                utility.clear_screen()
                print("===0 hints===")
            elif hint_choice == "n":
                utility.clear_screen()
                print("DID NOT USE HINT")
            else:
                utility.clear_screen()
                print("wrong input")
            print(f"Want to use word pass? (y/n) - {game.word_passes} available")
            pass_choice = input("> ").lower().strip()
            if pass_choice == "y" and game.word_passes > 0:
                game.word_passes -= 1
                utility.word_pass = game.word_passes
                print(f"The word is: {currentword} ")
            
            input("\nPress Enter to continue...")


# same lang code basically ung oop lang iba
def Quote_builder():
    """Play quote builder mode"""
    game = OOP.QuoteBuilderMode()
    utility.clear_screen()

    print("="*40)
    print("QOUTE BUILDER MODE")
    print("="*40)


    # condition para mag loop
    while not game.is_game_over() and not game.is_victory():
        utility.clear_screen()
        #kuha ng health saoop na galing naman sa utility
        print("=============QUOTE BUILDER MODE=============")
        print(f"\nHealth: {game.health} |  Score: {game.score} |  Hints: {game.hints} |  Passes: {game.word_passes}\n")
        print(f"{game.get_mode_info()}\n")
        print("="*40)

        #istore ung scrable
        currentword=game.get_current_word()
        scrambled = game.scramble_word(currentword)
        print(f"UNSCRAMBLE: {scrambled}")
        
        answer = input("ANSWER: ").lower().strip()

        if game.check_answer(answer,currentword):
            print("\nCORRECT\n")
            utility.score = game.score
            game.score +=1
            utility.mode2_score = max(utility.mode2_score, game.score)
            reward = game.give_reward()

            # incase of level up
            complete_msg = game.next_word()
            if complete_msg:
                print(f"\n{complete_msg}")
                print(f"\nFULL QUOTE: {game.get_complete_quote()} ")
                print(f"\nFINAL SCORE: {game.score} ")
                input("\nPress Enter to continue...")
                return
            else:
                print("\nPress any key to continue...")
                input()
        else:
            print("wrong answer")
            game.health -=1

            if game.is_game_over():
                utility.clear_screen()
                print(f"\nGAME OVER! Final Score: {game.score} ")
                print(f"The correct word was: {currentword}")
                print("\nPress any key to go back...")
                input()
                return
            utility.clear_screen()
            print(f"\nWant to use a hint? (y/n) - {game.hints} hints available")
            hint_choice = input("> ").lower().strip()
            if hint_choice == "y" and game.hints> 0:
                utility.clear_screen()
                hint = game.show_hint(currentword)
                if hint:
                    print(f"UNSCRAMBLE: {scrambled}")
                    print(f"🔍 Hint: {hint}")
            elif game.hints <= 0:
                print("===0 hints===")
            elif hint_choice == "n":
                utility.clear_screen()
                print("DID NOT USE HINT")
            else:
                print("wrong input")

            print(f"\nWant to use word pass? (y/n) - {game.word_passes} available")
            pass_choice = input("> ").lower()
            if pass_choice == 'y' and game.word_passes > 0:
                game.word_passes -= 1
                utility.word_pass = game.word_passes
                print(f"\nThe word is: {currentword} ")
            
            input("\nPress Enter to continue...")

#same lang basically ibang oop lang gamit nya
def extreme():
    """EXTREME difficulty"""
    game = OOP.ExtremeMode()
    utility.clear_screen()

    print("="*40)
    print("EXTREME MODE")
    print("="*40)
    # condition para mag loop
    while not game.is_game_over() and not game.is_victory():
        utility.clear_screen()
        #kuha ng health saoop na galing naman sa utility
        print(f"\nHealth: {game.health} |  Score: {game.score} |  Hints: {game.hints} |  Passes: {game.word_passes}\n")
        print(f"{game.get_mode_info()}\n")
        print("="*40)

        #istore ung scrable
        currentword=game.get_current_word()
        scrambled = game.scramble_word(currentword)
        print(f"UNSCRAMBLE: {scrambled}")
        
        answer = input("ANSWER: ").lower().strip()

        if game.check_answer(answer,currentword):
            print("\nCORRECT\n")
            utility.score = game.score
            game.score +=1
            utility.mode3_score = max(utility.mode3_score, game.score)
            reward = game.give_reward()

            # incase of level up
            level_up = game.next_word()
            if level_up:
                print(f"{level_up}")
                if "VICTORY" in level_up:
                    print(f"FINAL SCORE: {game.score} ")
                    input("\nPress Enter to continue...")
                    return
                input("Press Enter to continue...")
            else:
                print("\nPress any key to continue...")
                input()
        else:
            print("wrong answer")
            game.health -=1

            if game.is_game_over():
                utility.clear_screen()
                print(f"\n GAME OVER! Final Score: {game.score} ")
                print(f"The correct word was: {currentword}")
                print("\nPress any key to go back...")
                input()
                return
            utility.clear_screen()
            print(f"\nWant to use a hint? (y/n) - {game.hints} hints available")
            hint_choice = input("choice:").lower().strip()
            if hint_choice == "y" and game.hints> 0:
                utility.clear_screen()
                hint = game.show_hint(currentword)
                if hint:
                    print(f"UNSCRAMBLE: {scrambled}")
                    print(f"🔍 Hint: {hint}")
            elif game.hints <= 0:
                print("=== no more hints left ===")
            elif hint_choice == "n":
                utility.clear_screen()
                print("DID NOT USE HINT")
            else:
                print("wrong input")

            print(f"\n Want to use word pass? (y/n) - {game.word_passes} available")
            pass_choice = input().lower()
            if pass_choice == 'y' and game.word_passes > 0:
                game.word_passes -= 1
                utility.word_pass = game.word_passes
                print(f" The word is: {currentword} ")
            
            input("\nPress Enter to continue...")


def main():
    while True:
        utility.clear_screen()
        utility.welcome()
        print("\n======== THE WORD SCRAMBLE GAME ========\n")
        print("1. GAME MODES")
        print("2. RULES")
        print("3. EXIT\n")
        print("="*40)
        
        choice =input("Enter your Choice: ")

        if choice=="1":
            utility.clear_screen()
            while True:
                utility.clear_screen()
                print("=============== GAME MODE ==============\n")
                print("1. INFINITE")
                print("2. QOUTE BUILDER")
                print("3. EXTREME")
                print("4. BACK\n")
                print("="*40)

                choice1 = input("Enter your Choice: ")
                if choice1=="1":
                    while True:
                        utility.clear_screen()
                        print("=============INFINITE MODE=============\n")
                        print("1. START GAME")
                        print("2. GAME RULES")
                        print("3. HIGH SCORES")
                        print("4. BACK\n")
                        print("="*40)
                        choice2 = input("Enter your Choice: ")
                        if choice2=="1":
                            utility.clear_screen()
                            classic_play()
                        elif choice2=="2":
                            utility.clear_screen()
                            utility.rules_mode1()
                            print("\nPress Enter to go back")
                            input()
                        elif choice2=="3":
                            utility.clear_screen()
                            print("=============HIGH SCORES=============\n")
                            print(f"INFINITE MODE HIGH SCORE: {utility.mode1_score}")
                            print("="*40)
                            print("\nPress Enter to go back")
                            input()
                        elif choice2=="4":
                            utility.clear_screen()
                            break
                        else:
                            utility.clear_screen()
                            print("wrong input")
                elif choice1=="2":
                    while True:
                        utility.clear_screen()
                        print("=============QUOTE BUILDER MODE=============\n")
                        print("1. START GAME")
                        print("2. GAME RULES")
                        print("3. HIGH SCORES")
                        print("4. BACK\n")
                        print("="*40)
                        choice2 = input("Enter your Choice: ")
                        if choice2=="1":
                            utility.clear_screen()
                            Quote_builder()
                        elif choice2=="2":
                            utility.clear_screen()
                            utility.rules_mode2()
                            print("\nPress Enter to go back")
                            input()
                        elif choice2=="3":
                            utility.clear_screen()
                            print("=============HIGH SCORES=============\n")
                            print(f"QUOTE BUILDER MODE HIGH SCORE: {utility.mode2_score}")
                            print("="*40)
                            print("\nPress Enter to go back")
                            input()
                        elif choice2=="4":
                            utility.clear_screen()
                            break
                        else:
                            utility.clear_screen()
                            print("wrong input")
                elif choice1=="3":
                    while True:
                        utility.clear_screen()
                        print("=============EXTREME MODE=============\n")
                        print("1. START GAME")
                        print("2. GAME RULES")
                        print("3. HIGH SCORES")
                        print("4. BACK\n")
                        print("="*40)
                        choice2 = input("Enter your Choice: ")
                        if choice2=="1":
                            utility.clear_screen()
                            extreme()
                        elif choice2=="2":
                            utility.clear_screen()
                            utility.rules_mode3()
                            print("\nPress Enter to go back")
                            input()
                        elif choice2=="3":
                            utility.clear_screen()
                            print("=============HIGH SCORES=============\n")
                            print(f"EXTREME MODE HIGH SCORE: {utility.mode3_score}")
                            print("="*40)
                            print("\nPress Enter to go back")
                            input()
                        elif choice2=="4":
                            utility.clear_screen()
                            break
                        else:
                            utility.clear_screen()
                            print("wrong input")
                elif choice1=="4":
                    utility.clear_screen()
                    break
                else:
                    utility.clear_screen()
                    print("wrong input")
        elif choice == "2":
            utility.clear_screen()
            utility.rules()
            print("\nPress Enter to go back")
            input()
            utility.clear_screen()
        elif choice=="3":
            utility.clear_screen()
            print ("Thank you for playing our game!")
            break
        else:
            print("wrong input")

if __name__ == "__main__":
    main()