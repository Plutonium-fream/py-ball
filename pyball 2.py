# pyball 2.6 (179 Lines) The game is way harder now, and i patched an exploit
# have fun!

import random
import time

presetq = None
mode = None


def intro():
    global presetq, mode
    introart = """
       
 ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄               ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄                
▐░░░░░░░░░░░▌▐░▌       ▐░▌             ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░▌          ▐░▌               
▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌             ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌          ▐░▌               
▐░▌       ▐░▌▐░▌       ▐░▌             ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌               
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌          ▐░▌               
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░▌          ▐░▌               
▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌          ▐░▌               
▐░▌               ▐░▌                  ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌               
▐░▌               ▐░▌                  ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄      
▐░▌               ▐░▌                  ▐░░░░░░░░░░▌ ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     
 ▀                 ▀                    ▀▀▀▀▀▀▀▀▀▀   ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀      
                                                                                                

    """
    print(introart)
    print("******************")
    print("welcome to pyball!")
    print("******************")

    presetq = input("Do you want to choose a difficulty (d) or customize the stats yourself (c)? ").lower()

    if presetq == "d":
        mode = input("Very well, do you want easy (1), medium (2), hard (3), or EXTREME (4) mode? ")
    elif presetq == "c":
        print("Very well, customize the stats below!")
    else:
        print("Not a valid option, you need to type d or c")
        intro()


def goalart():
    artprint = """
 ██████╗  ██████╗  █████╗ ██╗     ██╗██╗██╗
██╔════╝ ██╔═══██╗██╔══██╗██║     ██║██║██║
██║  ███╗██║   ██║███████║██║     ██║██║██║
██║   ██║██║   ██║██╔══██║██║     ╚═╝╚═╝╚═╝
╚██████╔╝╚██████╔╝██║  ██║███████╗██╗██╗██╗
 ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝╚═╝╚═╝
                                           
"""
    print(artprint)


def main():
    global presetq, mode

    if presetq == "d":
        if mode == "1":
            player_level = 8
            gk_level = 3
            defense_alg = 4
        elif mode == "2":
            player_level = 6
            gk_level = 5
            defense_alg = 6
        elif mode == "3":
            player_level = 5
            gk_level = 6
            defense_alg = 7
        elif mode == "4":
            player_level = 1
            gk_level = 9
            defense_alg = 8
        else:
            print("Not a valid option, you need to choose between 1, 2, 3, and 4")
            intro()
    else:
        player_level = int(input("Your player's ALG: "))
        gk_level = int(input("Your Goalkeeper's ALG: "))
        defense_alg = int(input("ALG of the enemy team's defense: "))

    defensive_right = random.randint(1, 10) + defense_alg
    defensive_left = random.randint(1, 10) + defense_alg
    defensive_central = random.randint(1, 10) + defense_alg

    pitch = """
    +------------------------------------------------------------------+
    |                                                                  |
    |------------------------------------------------------------------|
    |                                                                  |
    |                                                                  |
    |                         how do you go?                           |
    |                                                                  |
    |                                                                  |
    |                                                                  |
    |                                                                  |
    |        Left                 center                 Right         |
    |                                                                  |
    |                                                                  |
    |                                                                  |
    |                                                                  |
    |                    |------------------------|                    |
    |                    |          Goal          |                    |
    |                    |------------------------|                    |
    +------------------------------------------------------------------+
    """
    print(pitch)
    defway = input("Do you want to go through the center, the left, or the right? ").lower()

    if defway == "center":
        momentum = 30 - defensive_central
    elif defway == 'right':
        momentum = 30 - defensive_right
    else:
        momentum = 30 - defensive_left

    print(f"You have {momentum} momentum left!")

    print("You arrive at the goal, it's a 1v1 against the goalkeeper")

    def print_football_goal():
        goal = """
         0   1   2   3   4   5   6   7   8   9
      +---+---+---+---+---+---+---+---+---+---+
    0 |   |   |   |   |   |   |   |   |   |   | 0
      +---+---+---+---+---+---+---+---+---+---+
    1 |   |   |   |   | G | G | G |   |   |   | 1
      +---+---+---+---+---+---+---+---+---+---+
    2 |   |   |   | G | G | GK| G | G |   |   | 2
      +---+---+---+---+---+---+---+---+---+---+
    3 |   |   |   |   | G | G | G |   |   |   | 3
      +---+---+---+---+---+---+---+---+---+---+
    4 |   |   |   |   |   |   |   |   |   |   | 4
      +---+---+---+---+---+---+---+---+---+---+
         0   1   2   3   4   5   6   7   8   9
        """
        print(goal)

    print_football_goal()
    shooting_coordinatesH = int(input("How high do you shoot? "))
    shooting_coordinatesL = int(input("Where do you want to shoot horizontally? "))
    average = (shooting_coordinatesH + shooting_coordinatesL) / 2
    average + 1
    averageWAY = random.randint(1, 2)
    if averageWAY == 2:
        if average >= 5:
            luck = random.randint(1, 5)
            momentum -= 5 + luck
            goalkeeper_savenumber = momentum + player_level - gk_level * 3
            if goalkeeper_savenumber > 0:
                print("GOAL!!!!")
                goalart()
                print("The goalkeeper went the right way but was too slow!")
            else:
                print("The goalkeeper saved the shot!")
        else:
            print("GOAL!!!!")
            goalart()
            print("The goalkeeper went the wrong way!")
    else:
        if average <= 5:
            luck = random.randint(1, 5)
            momentum -= 5 + luck
            goalkeeper_savenumber = momentum + player_level - gk_level * 3
            if goalkeeper_savenumber > 0:
                print("GOAL!!!!")
                goalart()
                print("The goalkeeper went the right way but was too slow!")
            else:
                print("The goalkeeper saved the shot!")
        else:
            print("GOAL!!!!")
            goalart
            print("The goalkeeper went the wrong way!")


def play_again():
    while True:
        answer = input("Do you want to play again? (yes/no): ").strip().lower()
        if answer in ['yes', 'y']:
            return True
        elif answer in ['no', 'n']:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


# Main game loop
while True:
    intro()
    main()
    if not play_again():
        print("Thank you for playing!")
        time.sleep(2)
        break
# pycharm test11
