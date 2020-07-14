import time
import random

def introduction_lines():

    print("You are in a land full of dragons. In front of you,")
    time.sleep(1)

    print("you see two caves. In one cave, the dragon is friendly")
    time.sleep(1)

    print("and will share his treasure with you. The other dragon")
    time.sleep(1)

    print("is greedy and hungry, and will eat you on sight.")
    time.sleep(1)

def main_game():

    print("Which cave will you go into? (1 or 2). Please enter your selection below")
    hungry_dragon  = random.randint(1,2)
    cave_choice = input()

    if cave_choice != 1 and cave_choice != 2:
        print("You have chosen an incorrect option, please try again")
        main_game()
    elif cave_choice == hungry_dragon:
        print("You approach the cave...")
        time.sleep(1)
        print("It is dark and spooky...")
        time.sleep(1)
        print("A large dragon jumps out in front of you! He opens his jaws and...")
        time.sleep(1)
        print("Gobbles you down in one bite! YOU LOSE")
        time.sleep(1)
        print("Would you like to play again? 1 or 0")
        replay = input()
        if replay == 1:
            main_game()
        else:
            print("Goodbye")
    else:
        print("You approach the cave...")
        time.sleep(1)
        print("It is dark and spooky...")
        time.sleep(1)
        print("A large dragon jumps out in front of you! He opens his jaws and...")
        time.sleep(1)
        print("Gives you his treasure! YOU WIN")
        time.sleep(1)
        print("Would you like to play again? 1 or 0")
        replay = input()
        if replay == 1:
            main_game()
        else:
            print("Goodbye")

introduction_lines()
main_game()