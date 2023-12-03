import glob

from .controls import Controls
from .db.scripts.migration import crete_db
from .game import Game
from .leaderboard import Leaderboard
from .menu import Menu
from .rules import Rules
from .settings import Settings


def main() -> None:
    '''Main function of the game, creates the settings, menu and game objects and runs main functions of them in the loop'''
    if not glob.glob("db.sqlite3"):
        crete_db()
    settings = Settings()
    menu = Menu(settings)
    game = Game(settings)
    leaderboard = Leaderboard(settings)
    controls = Controls(settings)
    rules = Rules(settings)
    while True:
        choice = menu.main()
        if choice == Menu.GAME_CHOICE:
            game.main()
        elif choice == Menu.LEADERBOARD_CHOICE:
            leaderboard.main()
        elif choice == Menu.CONTROLS_CHOICE:
            controls.main()
        elif choice == Menu.RULES_CHOICE:
            rules.main()


if __name__ == "__main__":
    main()
