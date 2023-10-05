# Create a new python program, call it Live.py.
# welcome(name)
# This function has a person name as an input and returns a string in the following layout:
# Hello <name> and welcome to the World of Games (WoG).
# Here you can find many cool games to play.



# This function prints out the following text:
# Please choose a game to play:
# 1. Memory Game - a sequence of numbers will appear for 1 second and you have to
# guess it back
# 2. Guess Game - guess a number and see if you chose like the computer
# 3. Currency Roulette - try and guess the value of a random amount of USD in ILS
# Gets an input from the user about the game he chose. After receiving the game number from
# the user, the function will get the level of difficulty with the following text and also save to a
# variable:
#
# Please choose game difficulty from 1 to 5:
# The function will check the input of the chosen game (the input suppose to be a number
# between 1 to 3), also will check the input of level of difficulty (input should be a number between
# 1 to 5).
import colorama
# from colorama import Fore, Back, Style
# import random
# from Guess_Game import Random_Game
# from rock_paper_sisccior import Rock_Game
# from Memory_Game import  appear_and_disappear
# from Score import add_score
# from LoadingScreen import loading_screen
# from ArtMode import TheDevilMode
# from run_app import stop_flask_server
# from run_app import start_flask_server
# def welcome(name):
#     player_name = input("Enter your name: ")
#
#     starting = print(f"hello : {player_name} and welcome to the game of (WoG)\nhere you can find many cool games to play: ")
#
#
# welcome("Playername")
#
# start_flask_server()
#
# def load_game():
#
#     while True:
#         game1 = "1. Guess Game - guess a number and see if you chose like the computer"
#         game2 = "2. Memory Game -On maintenance - a sequence of numbers will appear for 1 second and you have to guess it back"
#         game3 = "3. Rock Paper sisccior - try and guess the The write answe to Win the Computer"
#         stop_web_service ="Please press 4 to stop the web service"
#         game_selection = int(input(f"\n {game1}\n {game2}\n {game3}\n{stop_web_service}\n the game you choose :"))
#         difficaulty = "difficulty: "
#         user_game = "game: "
#     #     print(game_selection)
#     # #-------------------------------------------------------------------------------------------------------------
#         loading_screen(duration=3, interval=0.5)
#
#         if game_selection == 1:
#             diff = {1: 20, 2: 40, 3: 60, 4: 80, 5: 100}
#             print("you choose the game : Guess game")
#             d = int(input(f"Choose your difficulty 1-5 : "))
#             while d > 5 or d < 1:
#                 print("wrong number start again")
#                 d = int(input(f"Choose your difficulty 1-5 : "))
#             difficaulty = difficaulty + str(d)
#             user_game = user_game + str(game_selection)
#             print(f" {difficaulty} , {user_game}")
#             if d == 1:
#                 print("you choose difficaulty LVL 1: 1-20 ")
#             elif d == 2:
#                 print("you choose difficaulty LVL 2: 1-40 ")
#             elif d == 3:
#                 print("you choose difficaulty LVL 3: 1-60 ")
#             elif d == 4:
#                 print("you choose difficaulty LVL 4: 1-80 ")
#             elif d == 5:
#                 # print("you choose difficaulty LVL 5: 1-100 ")
#                 print(Fore.RED + 'you choose difficaulty LVL 5: 1-100\n ')
#                 print(f"Welcome to Hell Mode {TheDevilMode()}")
#             if Random_Game(diff[d]) == 1:
#                 add_score(d)
#
#
#     # -------------------------------------------------------------------------------------------------------------
#         elif game_selection == 2:
#             diff = {1: 5000, 2: 4000, 3: 3000, 4: 2000, 5: 1000}
#             num = random.randint(10000,99999)
#             print("ʕ•ᴥ•ʔ you choose the game : Memory Game ")
#             d = int(input(f"Choose your difficulty 1-5 : "))
#             while d > 5 or d < 1:
#                 print("wrong number start again")
#                 d = int(input(f"Choose your difficulty 1-5 : "))
#             difficaulty = difficaulty + str(d)
#             user_game = user_game + str(game_selection)
#             print(f" {difficaulty} , {user_game}")
#             if d == 1:
#                 print("you choose difficaulty LVL 1: you have 5000ms to remember the number ")
#             elif d == 2:
#                 print("you choose difficaulty LVL 2: you have 4000ms to remember the number  ")
#             elif d == 3:
#                 print("you choose difficaulty LVL 3: you have 3000ms to remember the number  ")
#             elif d == 4:
#                 print("you choose difficaulty LVL 4: you have 2000ms to remember the number  ")
#             elif d == 5:
#                 print("you choose difficaulty LVL 5: you have 1000ms to remember the number  ")
#             appear_and_disappear(num,diff[d])
#             try:
#                 User_Chose = int(input("write the number: "))
#             except ValueError:
#                 print("Thats not an int")
#                 continue
#             if User_Chose == num:
#                 print({"You Guess the number Right!! you Won"})
#                 add_score(d)
#             else:
#                 print("you Wrong please try again")
#
#
#     # -------------------------------------------------------------------------------------------------------------
#         elif game_selection == 3:
#             lvl = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
#             print("ʕ•ᴥ•ʔ you choose the game : Rock paper sisccior game  ")
#             d = int(input(f"Choose your difficulty 1-5 : "))
#             while d > 5 or d < 1:
#                 print("wrong number start again")
#                 d = int(input(f"Choose your difficulty 1-5 : "))
#             difficaulty = difficaulty + str(d)
#             user_game = user_game + str(game_selection)
#             print(f" {difficaulty} , {user_game}")
#             if d == 1:
#                 print("you choose difficaulty LVL 1: 1-Tries ")
#             elif d == 2:
#                 print("you choose difficaulty LVL 2: 2-Tries ")
#             elif d == 3:
#                 print("you choose difficaulty LVL 3: 3-Tries ")
#             elif d == 4:
#                 print("you choose difficaulty LVL 4: 4-Tries ")
#             elif d == 5:
#                 print("you choose difficaulty LVL 5: 5-Tries ")
#
#             if Rock_Game(lvl[d]) == 1:
#                 print("you Won")
#                 add_score(d)
#         elif game_selection == 4:
#             print("the web servier is Down ")
#             stop_flask_server()
#
#
#         else:
#             print("(☞ﾟヮﾟ)☞ you have to choose between 1-4 ☜(ﾟヮﾟ☜)")
#             load_game()
#
#
#
# load_game()
# Modified Live.py

import colorama
from colorama import Fore, Back, Style
import random
from Guess_Game import Random_Game
from rock_paper_sisccior import Rock_Game
from Memory_Game import appear_and_disappear
from Score import add_score
from LoadingScreen import loading_screen
from ArtMode import TheDevilMode
from run_app import stop_flask_server
from run_app import start_flask_server

# def welcome(name):
#     name = (input(f"Enter your name: "))
#     starting = print(f"hello : {name} and welcome to the game of (WoG)\nhere you can find many cool games to play: ")
#
# welcome("Playername")

start_flask_server()

def load_game():
    player_name = input("Enter your name: ")  # Collect the player's name

    while True:
        game1 = "1. Guess Game - guess a number and see if you chose like the computer"
        game2 = "2. Memory Game -On maintenance - a sequence of numbers will appear for 1 second and you have to guess it back"
        game3 = "3. Rock Paper sisccior - try and guess the The write answe to Win the Computer"
        stop_web_service ="Please press 4 to stop the web service"
        game_selection = int(input(f"\n {game1}\n {game2}\n {game3}\n{stop_web_service}\n the game you choose :"))
        difficaulty = "difficulty: "
        user_game = "game: "

        loading_screen(duration=3, interval=0.5)

        if game_selection == 1:
            diff = {1: 20, 2: 40, 3: 60, 4: 80, 5: 100}
            print("you choose the game : Guess game")
            d = int(input(f"Choose your difficulty 1-5 : "))
            while d > 5 or d < 1:
                print("wrong number start again")
                d = int(input(f"Choose your difficulty 1-5 : "))
            difficaulty = difficaulty + str(d)
            user_game = user_game + str(game_selection)
            print(f" {difficaulty} , {user_game}")
            if d == 1:
                print("you choose difficulty LVL 1: 1-20 ")
            elif d == 2:
                print("you choose difficulty LVL 2: 1-40 ")
            elif d == 3:
                print("you choose difficulty LVL 3: 1-60 ")
            elif d == 4:
                print("you choose difficulty LVL 4: 1-80 ")
            elif d == 5:
                print(Fore.RED + 'you choose difficulty LVL 5: 1-100\n ')
                print(f"Welcome to Hell Mode {TheDevilMode()}")
            if Random_Game(diff[d]) == 1:
                add_score(player_name, d)  # Save score by player name

        elif game_selection == 2:
            diff = {1: 5000, 2: 4000, 3: 3000, 4: 2000, 5: 1000}
            num = random.randint(10000, 99999)
            print("ʕ•ᴥ•ʔ you choose the game : Memory Game ")
            d = int(input(f"Choose your difficulty 1-5 : "))
            while d > 5 or d < 1:
                print("wrong number start again")
                d = int(input(f"Choose your difficulty 1-5 : "))
            difficaulty = difficaulty + str(d)
            user_game = user_game + str(game_selection)
            print(f" {difficaulty} , {user_game}")
            if d == 1:
                print("you choose difficulty LVL 1: you have 5000ms to remember the number ")
            elif d == 2:
                print("you choose difficulty LVL 2: you have 4000ms to remember the number  ")
            elif d == 3:
                print("you choose difficulty LVL 3: you have 3000ms to remember the number  ")
            elif d == 4:
                print("you choose difficulty LVL 4: you have 2000ms to remember the number  ")
            elif d == 5:
                print("you choose difficulty LVL 5: you have 1000ms to remember the number  ")
            appear_and_disappear(num, diff[d])
            try:
                User_Chose = int(input("write the number: "))
            except ValueError:
                print("That's not an int")
                continue
            if User_Chose == num:
                print("You Guess the number Right!! you Won")
                add_score(player_name, d)  # Save score by player name
            else:
                print("you Wrong please try again")

        elif game_selection == 3:
            lvl = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
            print("ʕ•ᴥ•ʔ you choose the game : Rock paper sisccior game  ")
            d = int(input(f"Choose your difficulty 1-5 : "))
            while d > 5 or d < 1:
                print("wrong number start again")
                d = int(input(f"Choose your difficulty 1-5 : "))
            difficaulty = difficaulty + str(d)
            user_game = user_game + str(game_selection)
            print(f" {difficaulty} , {user_game}")
            if d == 1:
                print("you choose difficulty LVL 1: 1-Tries ")
            elif d == 2:
                print("you choose difficulty LVL 2: 2-Tries ")
            elif d == 3:
                print("you choose difficulty LVL 3: 3-Tries ")
            elif d == 4:
                print("you choose difficulty LVL 4: 4-Tries ")
            elif d == 5:
                print("you choose difficulty LVL 5: 5-Tries ")
            if Rock_Game(lvl[d]) == 1:
                print("you Won")
                add_score(player_name, d)  # Save score by player name
        elif game_selection == 4:
            print("the web service is Down ")
            stop_flask_server()
        else:
            print("(☞ﾟヮﾟ)☞ you have to choose between 1-4 ☜(ﾟヮﾟ☜)")
            load_game()

load_game()


