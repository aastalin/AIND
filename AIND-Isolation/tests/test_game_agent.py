"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent

from importlib import reload
from game_agent import IsolationPlayer
from game_agent import MinimaxPlayer


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)

    def test_MinimaxPlayer(self):
        self.player1 = MinimaxPlayer()
        self.player2 = MinimaxPlayer()
        self.game = isolation.Board(self.player1, self.player2)

        assert(len(self.game.get_legal_moves())==49)

        self.game.apply_move((3,3))
        self.game.apply_move((0,4))
        assert(self.player1 == self.game.active_player)

        winner, history, outcome = self.game.play()
        win_str = 'player1' if winner==self.player1 else 'player2'
        print("\nWinner: {}\nOutcome: {}".format(win_str, outcome))
        print(self.game.to_string())
        print("Move history:\n{!s}".format(history))



if __name__ == '__main__':
    unittest.main()
