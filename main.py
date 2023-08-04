from game import Game
from menu import Menu
import time

def main():
    menu = Menu()
    while True:
        menu.main()
        game = Game()     
        game.main()

if __name__ == "__main__":
    main()
