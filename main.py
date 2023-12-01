from game import Game
from menu import Menu
from settings import Settings


def main() -> None:
    '''Main function of the game, creates the settings, menu and game objects and runs main functions of them in the loop'''
    settings = Settings()
    menu = Menu(settings)
    game = Game(settings)
    while True:
        menu.main()
        game.main()


if __name__ == "__main__":
    main()
