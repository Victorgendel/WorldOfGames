from selenium import webdriver
from time import sleep
import sys
# def test_scores_service(url):
#     driver1 = webdriver.Firefox()
#     driver1.get(url)
#     web_score = driver1.find_element('id','score')
#     print(web_score)
#
def test_scores_service():
    driver1 = webdriver.Chrome()
    driver1.get("http://127.0.0.1:5000/")
    sleep(5)
    login = driver1.find_element("xpath","/html/body/table/tbody/tr[2]/td[2]").text
    print(login)
    if 1 <= int(login) < 1000:
        return True
    else:
        return False

def main_function():
    if test_scores_service():
        print("Tests passed.")
        return sys.exit()
    else:
        print("Tests failed.")
        return sys.exit(-1)
print(main_function())