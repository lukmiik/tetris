import time

from settings import Settings
from menu import Menu
from game import Game


def main():
    settings = Settings()
    menu = Menu(settings)
    game = Game(settings)
    while True:
        menu.main()
        game.main()
        time.sleep(5)


if __name__ == "__main__":
    main()
