import random
from Score import add_score

def Rock_Game(deff):
    countplayer = 0
    countcumputer = 0
    while True:
        chooses = ("Rock", "Paper", "Scissors")
        CumputerChoose = random.choice(chooses)
        player = input("Please Enter Rock, Paper, Scissors: ")

        if player not in chooses:
            print("Invalid input. Please choose Rock, Paper, or Scissors.")
            continue

        if CumputerChoose == player:
            print(f"Both chose {player}. It's a tie.")
        elif CumputerChoose == "Rock" and player == "Paper":
            countplayer = countplayer + 1
            print(f"You win! \nPlayer Score is = {countplayer}\nComputer Score is : {countcumputer}")
        elif CumputerChoose == "Rock" and player == "Scissors":
            countcumputer = countcumputer + 1
            print(f"You Lost! \nPlayer Score is = {countplayer}\nComputer Score is : {countcumputer}")
        elif CumputerChoose == "Paper" and player == "Scissors":
            countplayer = countplayer + 1
            print(f"You win! \nPlayer Score is = {countplayer}\nComputer Score is : {countcumputer}")
        elif CumputerChoose == "Paper" and player == "Rock":
            countcumputer = countcumputer + 1
            print(f"You Lost! \nPlayer Score is = {countplayer}\nComputer Score is : {countcumputer}")
        elif CumputerChoose == "Scissors" and player == "Rock":
            countplayer = countplayer + 1
            print(f"You win! \nPlayer Score is = {countplayer}\nComputer Score is : {countcumputer}")


        elif CumputerChoose == "Scissors" and player == "Paper":
            countcumputer = countcumputer + 1
            print(f"You Lost! \nPlayer Score is = {countplayer}\nComputer Score is : {countcumputer}")

        if countplayer == deff:
            return 1
        elif countcumputer == deff:
            print("You Lose")
            break


