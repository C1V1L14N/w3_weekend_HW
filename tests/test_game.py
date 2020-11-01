import unittest

from app.models.game import *
from app.models.player import *
from app.models.selection import *
# from app.models.game import *

class TestGame(unittest.TestCase):
    

    def test_play_game(self):
        self.player_1 = Player("Dave", Selection.ROCK)
        self.player_2 = Player("Jeff", Selection.PAPER)
        self.assertEqual("Player 2 wins!", Game.play_game(self.player_1, self.player_2))

        # self.player_1 = Player("Dave", Selection.SCISSORS)
        # self.player_2 = Player("Jeff", Selection.PAPER)
        # self.game = Game(self.player_1, self.player_2)
        # self.assertEqual("Player 1 wins!", self.game.play_game())

        # self.player_1 = Player("Dave", Selection.ROCK)
        # self.player_2 = Player("Jeff", Selection.ROCK)
        # self.game = Game(self.player_1, self.player_2)
        # self.assertEqual("Ooooh, it's a draw!", self.game.play_game())
        


    