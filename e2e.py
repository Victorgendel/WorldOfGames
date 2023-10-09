from selenium import webdriver
from time import sleep
import sys

def test_scores_service():
    try:
        driver1 = webdriver.Firefox()
        driver1.get("http://127.0.0.1:5000/")
        sleep(5)
        login = driver1.find_element("xpath", "/html/body/table/tbody/tr[2]/td[2]").text
        print(login)
        if 1 <= int(login) < 1000:
            return True
        else:
            return False
    except Exception as e:
        print(f"There is no User Score yet please play a game: {e}")
        return False

def main_function():
    if test_scores_service():
        print("Tests passed.")
        return sys.exit()
    else:
        print("Tests failed.")
        return sys.exit(-1)


