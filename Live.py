import ast
import time


my_file = open("instructions.json")
info = dict(ast.literal_eval(my_file.read()))


def welcome_wog():
    player_name = input("Whats your name traveler? ")
    print(f"Hello {player_name}, \n"
          "welcome to the world of games (Wog) here you can find many cool games to play! \n")


def need_help():
    help_game = input("Great would you like to get instructions for this game? y/n ").lower()
    if help_game == "y":
        print(info["memory"])
    else:
        pass


def need_help2():
    help_game = input("Great would you like to get instructions for this game? y/n ").lower()
    if help_game == "y":
        print(info["guessing"])
    else:
        pass


def need_help3():
    help_game = input("Great would you like to get instructions for this game? y/n ").lower()
    if help_game == "y":
        print(info["currency"])
    else:
        pass


def load_game():
    time.sleep(1)
    print("Which game would you like to play?\n",
          "We have the following games to play:\n"
          "1.Memory game \n"
          "2.Guess Game \n"
          "3.Currency roulette")
    player_choice = int(input("Which game would you like to play? (1, 2 or 3)? "))
    if player_choice == 1:
        need_help()
    elif player_choice == 2:
        need_help2()
    elif player_choice == 3:
        need_help3()
    else:
        print("You didn't choose a valid option")
        load_game()


welcome_wog()
load_game()
