# from run_app import start_flask_server
def mainGame():
    from Live import welcome , load_game
    start_flask_server()
    print(welcome("yes"))
    load_game()
mainGame()