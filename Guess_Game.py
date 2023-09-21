# Guess game
from Score import add_score
def Random_Game(x):
    import random
    random =random.randint(1,x)
    count = 10
    while count != 0:
        try:
         num = int(input("Enter a number: "))
        except ValueError:
            print("Thats not an int")
            continue
        if num == random:
            print(f"you Right!! the number was : {num}\n▉▉▉▉▉◤┳┻┳◥▉▉▉▉▉\n▉▉▉▉◤┳┻┳┻┳◥▉▉▉▉\n▉▉▉◤┳━┳━┳━┳◥▉▉▉\n▉▉◤┳┃┈( ͡° ͜ʖ ͡°)┈┃┳◥▉▉\n▉◤┳┻╰━━━━━╯┻┳◥▉\n◤┳┻┳┻┳┻┳┻┳┻┳┻┳◥ ")

            return 1
        elif num < random:
            print("Guess Higher: ")
        elif num > random:
            print("Guess Lower: ")
        count = count -1
        print(f"Trys Left : {count}")
        if count == 0:
            print("You Lost")


