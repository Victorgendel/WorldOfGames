from colorama import Fore
import random
from Guess_Game import Random_Game
from rock_paper_sisccior import Rock_Game
from Memory_Game import memory_game
from Score import add_score
from LoadingScreen import loading_screen
from ArtMode import TheDevilMode
from run_app import stop_flask_server
from run_app import start_flask_server

def welcome(name):
    name = (input(f"Enter your name: "))
    print(f"hello  {name} and welcome to the game of (WoG)\nhere you can find many cool games to play: \n too see the score: http://localhost:5000/ ")

    return name

start_flask_server()

def load_game():
    player_name = welcome("name")  # Collect the player's name

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
            diff = {1: 3, 2: 6, 3: 9, 4: 12, 5: 15}
            print("ʕ•ᴥ•ʔ you choose the game : Memory Game ")
            d = int(input(f"Choose your difficulty 1-5 : "))
            while d > 5 or d < 1:
                print("wrong number start again")
                d = int(input(f"Choose your difficulty 1-5 : "))
            difficaulty = difficaulty + str(d)
            user_game = user_game + str(game_selection)
            print(f" {difficaulty} , {user_game}")
            if d == 1:
                print("you choose difficulty LVL 1: you have 3 numbers  to remember ")
            elif d == 2:
                print("you choose difficulty LVL 2: you have 6 numbers  to remember   ")
            elif d == 3:
                print("you choose difficulty LVL 3: you have 9 numbers  to remember   ")
            elif d == 4:
                print("you choose difficulty LVL 4: you have 12 numbers  to remember   ")
            elif d == 5:
                print("you choose difficulty LVL 5: you have 15 numbers  to remember  ")
            if memory_game(diff[d]) == 1:
                add_score(player_name, d)  # Save score by player name


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


