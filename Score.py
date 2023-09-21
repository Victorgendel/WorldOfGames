import os


def add_score(score):
    POINTS_OF_WINNING = (score * 3) + 5
    check = os.listdir(".")
    if "score.txt" in check:
        file = open("score.txt", "a+")
        file.write(str(POINTS_OF_WINNING) + ",")
        file.close()
    else:
        file = open("score.txt", "w+")
        file.write(str(POINTS_OF_WINNING) + ",")
        file.close()
