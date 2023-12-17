from unittest import TestCase
from unittest.mock import patch

from tetris.menu import Menu
from tetris.settings import Settings


class TestMenu(TestCase):
    '''
    Test case class for testing the Menu class.
    '''

    def setUp(self) -> None:
        self.settings = Settings()
        self.menu = Menu(self.settings)

    @patch('menu.Menu.check_events')
    @patch('menu.Menu.check_hover')
    @patch('menu.Menu.draw_buttons')
    @patch('menu.pygame.display.update')
    def test_main(
        self,
        mock_display_update,
        mock_draw_buttons,
        mock_check_hover,
        mock_check_events,
    ) -> None:
        mock_check_events.side_effect = [False, True]
        self.menu.main()
        mock_check_events.assert_called()
        mock_check_hover.assert_called()
        mock_draw_buttons.assert_called()
        mock_display_update.assert_called()
