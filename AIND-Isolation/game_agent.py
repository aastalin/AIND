"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random


class SearchTimeout(Exception):
    pass

def custom_score(game, player):
    return len(game.get_legal_moves())


def custom_score_2(game, player):
    return len(game.get_legal_moves())


def custom_score_3(game, player):
    return len(game.get_legal_moves())


class IsolationPlayer:
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):

    def get_move(self, game, time_left):
        self.time_left = time_left
        best_move = (-1, -1)

        try:
            return self.minimax(game, self.search_depth)
        except SearchTimeout:
            pass
        return best_move

    def terminal_test(self, game):
        moves_available = bool(game.get_legal_moves())
        return not moves_available

    def min_value(self, game, depth):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        if depth == 0:
            return self.score(game, game.active_player)

        v = float("inf")
        for m in game.get_legal_moves():
            v = min(v, self.max_value(game.forecast_move(m), depth-1))
        return v

    def max_value(self, game, depth):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        if depth == 0:
            return self.score(game, game.active_player)
    
        v = float("-inf")
        for m in game.get_legal_moves():
            v = max(v, self.min_value(game.forecast_move(m), depth-1))
        return v

    def minimax(self, game, depth):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        best_move = (-1, -1)
        best_score = float("-inf")

        for m in game.get_legal_moves():
            v = self.min_value(game.forecast_move(m), depth-1)
            if v >= best_score:
                best_score = v
                best_move = m
        return best_move


class AlphaBetaPlayer(IsolationPlayer):

    def get_move(self, game, time_left):
        self.time_left = time_left
        best_move = (-1, -1)

        try:
            depth = 0
            while True:
                best_move = self.alphabeta(game, depth)
                depth += 1
        except SearchTimeout:
            pass
        except Terminal:
            pass
        return best_move

    def min_value(self, game, depth, alpha, beta):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        if depth == 0:
            return self.score(game, game.active_player)

        v = float("inf")
        for m in game.get_legal_moves():
            v = min(v, self.max_value(game.forecast_move(m), depth-1, alpha, beta))
            if v<= alpha: return v
            beta = min(beta, v)
        return v

    def max_value(self, game, depth, alpha, beta):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        if depth == 0:
            return self.score(game, game.active_player)

        v = float("-inf")
        for m in game.get_legal_moves():
            v = max(v, self.min_value(game.forecast_move(m), depth-1, alpha, beta))
            if v>= beta: return v
            alpha = max(alpha, v)
        return v

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        best_move = (-1, -1)
        best_score = float("-inf")

        for m in game.get_legal_moves():
            v = self.min_value(game.forecast_move(m), depth-1, alpha, beta)
            if v > best_score:
                best_score = v
                best_move = m
        return best_move

