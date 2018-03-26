"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest
import timeit
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

#    def test_MinimaxPlayer(self):
#        self.player1 = MinimaxPlayer()
#        self.player2 = MinimaxPlayer()
#
#        time_millis = lambda: 1000 * timeit.default_timer()
#        move_start = time_millis()
 #       time_left = lambda : 150 - (time_millis() - move_start)
#        self.player1.time_left = time_left
#        self.player2.time_left = time_left
#
#        self.game = isolation.Board(self.player1, self.player2)
#
#        assert(len(self.game.get_legal_moves())==49)
#
#        self.game.apply_move((3,3))
#        while True:
#            # player2
#            best_move = self.player2.minimax(self.game, 1)
#            if best_move == (-1, -1): break
#            self.game.apply_move(best_move)
#            # player1
#            best_move = self.player1.minimax(self.game, 1)
#            if best_move == (-1, -1): break
#            self.game.apply_move(best_move)
#        assert(len(self.game.get_legal_moves())==0)

    def test_MinimaxFailCase(self):
        self.player1 = MinimaxPlayer()
        self.player2 = MinimaxPlayer()

        time_millis = lambda: 1000 * timeit.default_timer()
        move_start = time_millis()
        time_left = lambda : 150 - (time_millis() - move_start)
        self.player1.time_left = time_left
        self.player2.time_left = time_left

        self.game = isolation.Board(self.player1, self.player2, 9, 9)
        self.game._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 59, 30]

        print(self.game.to_string())
        best_move = self.player1.minimax(self.game, 1)


if __name__ == '__main__':
    unittest.main()
