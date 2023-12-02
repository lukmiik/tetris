from controls import Controls
from game import Game
from leaderboard import Leaderboard
from menu import Menu
from settings import Settings


def main() -> None:
    '''Main function of the game, creates the settings, menu and game objects and runs main functions of them in the loop'''
    settings = Settings()
    menu = Menu(settings)
    game = Game(settings)
    leaderboard = Leaderboard(settings)
    controls = Controls(settings)
    while True:
        choice = menu.main()
        if choice == Menu.GAME_CHOICE:
            game.main()
        elif choice == Menu.LEADERBOARD_CHOICE:
            leaderboard.main()
        elif choice == Menu.CONTROLS_CHOICE:
            controls.main()
        elif choice == Menu.RULES_CHOICE:
            pass


if __name__ == "__main__":
    main()
