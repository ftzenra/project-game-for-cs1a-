import random
import randomizer
import Datamodule
import utility
import OOP

def classic_play():
    """Playingfinite mode with rising difficulty"""
    game = OOP.InfiniteMode()
    utility.clear_screen()

    print("="*40)
    print("INFINITE MODE")
    print("="*40)
    # condition para mag loop
    while not game.is_game_over() and not game.is_victory():
        utility.clear_screen()
        #kuha ng health saoop na galing naman sa utility
        print(f"\n Health: {game.health} |  Score: {game.score} |  Hints: {game.hints} |  Passes: {game.word_passes}")
        print (game.get_mode_info())
        print("="*40)

        #istore ung scrable
        currentword=game.get_current_word()
        scrambled = game.scramble_word(currentword)
        print(f"UNSCRAMBLE: {scrambled}")
        
        answer = input("input answer: ").lower().strip()

        if game.check_answer(answer,currentword):
            print("CORRECT")
            utility.score = game.score
            game.score +=1

            reward = game.give_reward()
            print(f"your got random gift {reward}")

            # incase of level up
            level_up = game.next_word()
            if level_up:
                print({level_up})
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

            print(f"\n Want to use a hint? (y/n) - {game.hints} hints available")
            hint_choice = input("choice:").lower().strip()
            if hint_choice == "y" and game.hints> 0:
                utility.clear_screen()
                hint = game.show_hint(currentword)
                if hint:
                    print(f"🔍 Hint: {hint}")
            elif game.hints <= 0:
                print("===0 hints===")
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


def Qoute_builder():
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
        print(f"\n Health: {game.health} |  Score: {game.score} |  Hints: {game.hints} |  Passes: {game.word_passes}")
        print (game.get_mode_info())
        print("="*40)

        #istore ung scrable
        currentword=game.get_current_word()
        scrambled = game.scramble_word(currentword)
        print(f"UNSCRAMBLE: {scrambled}")
        
        answer = input("input answer: ").lower().strip()

        if game.check_answer(answer,currentword):
            print("CORRECT")
            utility.score = game.score
            game.score +=1

            reward = game.give_reward()
            print(f"your got random gift {reward}")

            # incase of level up
            complete_msg = game.next_word()
            if complete_msg:
                print(f"\n{complete_msg}")
                print(f"\n FULL QUOTE: {game.get_complete_quote()} ")
                print(f"\n FINAL SCORE: {game.score} ")
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
                print(f"\n GAME OVER! Final Score: {game.score} ")
                print(f"The correct word was: {currentword}")
                print("\nPress any key to go back...")
                input()
                return

            print(f"\n Want to use a hint? (y/n) - {game.hints} hints available")
            hint_choice = input("choice:").lower().strip()
            if hint_choice == "y" and game.hints> 0:
                utility.clear_screen()
                hint = game.show_hint(currentword)
                if hint:
                    print(f"🔍 Hint: {hint}")
            elif game.hints <= 0:
                print("===0 hints===")
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

def extreme():
    """Play extreme mode with long words"""
    game = OOP.ExtremeMode()
    utility.clear_screen()
    
    print("="*40)
    print(" EXTREME MODE - Long words, limited help! ")
    print("="*40)
    
    while not game.is_game_over() and not game.is_victory():
        utility.clear_screen()
        print(f"\n Health: {game.health} |  Score: {game.score} |  Hints: {game.hints} |  Passes: {game.word_passes}")
        print(f"{game.get_mode_info()}")
        print("-" * 40)
        
        current_word = game.get_current_word()
        scrambled = game.scramble_word(current_word)
        print(f"Unscramble ({len(current_word)} letters): {scrambled}")
        
        answer = input(" Your answer: ").lower().strip()
        
        if game.check_answer(answer, current_word):
            print("\n CORRECT! ")
            game.score += 1
            utility.score = game.score
            
            # Use randomizer's gift system
            reward = game.give_reward()
            print(f" You got a random gift: {reward} ")
            
            # Move to next word
            complete_msg = game.next_word()
            if complete_msg:
                print(f"\n{complete_msg}")
                print(f"\n🏆 FINAL SCORE: {game.score} 🏆")
                input("\nPress Enter to continue...")
                return
            else:
                print("\nPress any key to continue...")
                input()
        else:
            print(f"\n WRONG! Answer")
            game.health -= 1
            utility.health = game.health
            print(f" Health: {game.health}")
            
            if game.is_game_over():
                print(f"\n GAME OVER! Final Score: {game.score} ")
                print(f"The correct word was: {current_word}")
                print("\nPress any key to go back...")
                input()
                return
            
            # Hint option (only 1 hint in extreme mode)
            if game.hints > 0:
                print(f"\n Want to use a hint? (y/n) - {game.hints} hint available")
                hint_choice = input().lower()
                if hint_choice == 'y':
                    utility.clear_screen()
                    hint = game.show_hint(current_word)
                    if hint:
                        print(f"🔍 Hint: {hint}")
            elif game.hints <= 0:
                print("===0 hints===")
            
            # Word pass option
            if game.word_passes > 0:
                print(f"\n Want to use word pass? (y/n) - {game.word_passes} available")
                pass_choice = input().lower()
                if pass_choice == 'y':
                    game.word_passes -= 1
                    utility.word_pass = game.word_passes
                    print(f" The word is: {current_word}")
            
            input("\nPress Enter to continue...")

def main():
    while True:
        utility.clear_screen
        utility.welcome
        print("===============CS1A GAME================")
        print("="*40)
        print("1.GAME MODES")
        print("2.RULES")
        print("3.EXIT")
        print("="*40)
        
        choice =input("Enter your Choice: ")

        if choice=="1":
            utility.clear_screen()
            while True:
                utility.clear_screen()
                print("===============GAME MODE================")
                print("1.INFINITE")
                print("2.QOUTE BUILDER")
                print("3.EXTREME")
                print("4.BACK")
                print("="*40)

                choice1 = input("Enter your Choice: ")
                if choice1=="1":
                    utility.clear_screen()
                    classic_play()
                elif choice1=="2":
                    utility.clear_screen()
                    Qoute_builder()
                elif choice1=="3":
                    utility.clear_screen()
                    extreme()
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
        elif choice==3:
            print ("thank you for playing")
        else:
            print("wrong input")

if __name__ == "__main__":
    main()




  



