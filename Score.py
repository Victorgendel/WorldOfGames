
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
