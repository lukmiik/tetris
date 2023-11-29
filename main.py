import time

from game import Game
from menu import Menu
from settings import Settings


def main() -> None:
    settings = Settings()
    menu = Menu(settings)
    game = Game(settings)
    while True:
        menu.main()
        game.main()
        time.sleep(3)


if __name__ == "__main__":
    main()
