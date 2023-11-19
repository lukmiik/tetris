from game import Game
from menu import Menu
import time


def main():
    menu = Menu()
    while True:
        menu.main()
        game = Game()
        game.main()
        time.sleep(5)


if __name__ == "__main__":
    main()
