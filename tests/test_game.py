# tests/test_game.py
from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
            # setup
            new_game = Game()

            # exercise
            grid = new_game.grid

            # verify
            assert isinstance(grid, list)
            assert len(grid) == 9
            for letter in grid:
                assert letter in string.ascii_uppercase

    def test_is_valid(self):
            # setup
            new_game = Game()
            test_grid = 'KWEUEAKRZ'
            test_word = 'EUREKA'
            # exercise
            new_game.grid = list(test_grid) # Force the grid to a test case
            # verify
            assert new_game.is_valid(test_word) is True
            # teardown
            assert new_game.grid == list(test_grid) # Make sure the grid remained untouched
