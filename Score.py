import os


# def add_score(score):
#     POINTS_OF_WINNING = (score * 3) + 5
#     check = os.listdir(".")
#     if "Scores.txt" in check:
#         file = open("Scores.txt", "a+")
#         file.write(str(POINTS_OF_WINNING) + ",")
#         file.close()
#     else:
#         file = open("Scores.txt", "w+")
#         file.write(str(POINTS_OF_WINNING) + ",")
#         file.close()

import os
#
# def add_score(difficulty):
#     POINTS_OF_WINNING = (difficulty * 3) + 5
#
#     # Check if the Scores.txt file exists
#     if os.path.exists("Scores.txt"):
#         # Read the current score
#         with open("Scores.txt", "r") as file:
#             content = file.read().strip()
#             current_score = int(content) if content else 0
#         # Calculate the new total score
#         total_score = current_score + POINTS_OF_WINNING
#         # Update the Scores.txt file with the new score
#         with open("Scores.txt", "w") as file:
#             file.write(str(total_score))
#         print("Score successfully updated.")
#     else:
#         # Create the Scores.txt file and write the initial score
#         with open("Scores.txt", "w") as file:
#             file.write(str(POINTS_OF_WINNING))
#         print("Scores.txt created with initial score.")

#--------------------------------------------------------------------------------------------
import os

def add_score(player_name, score):
    # Calculate the new score
    new_score = (score * 3) + 5
    scores = {}

    # Check if the Scores.txt file exists
    if os.path.exists("Scores.txt"):
        # Read the current scores from the file
        with open("Scores.txt", "r") as file:
            content = file.read().strip()
            if content:
                scores = eval(content)

    # Update the player's score
    scores[player_name] = scores.get(player_name, 0) + new_score

    # Write the updated scores back to the file
    with open("Scores.txt", "w") as file:
        file.write(str(scores))

    print("Score successfully updated.")
