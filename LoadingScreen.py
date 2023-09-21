
import colorama
import sys
import time
from colorama import Fore  # Import the Fore module from colorama

# Initialize colorama
colorama.init()

def loading_screen(duration, interval):
    start_time = time.time()
    while time.time() - start_time < duration:
        sys.stdout.write(Fore.GREEN + "\rLoading Game" + "." * (int(time.time() * 2) % 4) + "   ")
        sys.stdout.flush()
        time.sleep(interval)

    sys.stdout.write("\rLoading complete!        \n")
    sys.stdout.flush()

# Call the loading_screen function
