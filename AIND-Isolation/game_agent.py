"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random
import math

class SearchTimeout(Exception):
    pass

def get_future_moves(game, player):
    directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                  (1, -2), (1, 2), (2, -1), (2, 1)]

    next_moves = []
    for loc in game.get_legal_moves(player):
        r, c = loc
        moves = [(r + dr, c + dc) for dr, dc in directions
                if game.move_is_legal((r + dr, c + dc))]
        for m in moves: next_moves.append(m)
    random.shuffle(next_moves)
    return next_moves

def custom_score(game, player):
    my_score = len(get_future_moves(game, player))
    op_score = len(get_future_moves(game, game.get_opponent(player)))
    return float(my_score - op_score)


def custom_score_2(game, player):
    my_moves = get_future_moves(game, player)
    op_moves = get_future_moves(game, game.get_opponent(player))

    ct0 = math.ceil(game.width /2)-1
    ct1 = math.ceil(game.height/2)-1

    good_my_moves = [m for m in my_moves if not game.move_is_legal((2*ct0-m[0], 2*ct1-m[1]))]
    good_op_moves = [m for m in op_moves if not game.move_is_legal((2*ct0-m[0], 2*ct1-m[1]))]
    return float(len(good_my_moves)-len(good_op_moves))


def custom_score_3(game, player):
    my_moves = game.get_legal_moves(player)
    op_moves = game.get_legal_moves(game.get_opponent(player))
 
    ct0 = math.ceil(game.width /2)-1
    ct1 = math.ceil(game.height/2)-1

    good_my_moves = [m for m in my_moves if not game.move_is_legal((2*ct0-m[0], 2*ct1-m[1]))]
    good_op_moves = [m for m in op_moves if not game.move_is_legal((2*ct0-m[0], 2*ct1-m[1]))]
    return float(len(my_moves)+len(good_my_moves)-len(good_op_moves))


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

    def min_value(self, game, depth):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        v = float("inf")
        for m in game.get_legal_moves():
            if depth == 0:
                v = min(v, self.score(game, self))
            else:
                v = min(v, self.max_value(game.forecast_move(m), depth-1))
        return v

    def max_value(self, game, depth):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
    
        v = float("-inf")
        for m in game.get_legal_moves():
            if depth == 0:
                v = max(v, self.score(game, self))
            else:
                v = max(v, self.min_value(game.forecast_move(m), depth-1))
        return v

    def minimax(self, game, depth):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        best_move = (-1, -1)
        best_score = float("-inf")
        for m in game.get_legal_moves():
            if depth == 0:
                v = self.score(game, self)
            else:
                v = self.min_value(game.forecast_move(m), depth-1)
            if v > best_score:
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
            return best_move
        return best_move

    def min_value(self, game, depth, alpha, beta):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        v = float("inf")
        for m in game.get_legal_moves():
            if depth == 0:
                v = min(v, self.score(game, self))
            else:
                v = min(v, self.max_value(game.forecast_move(m), depth-1, alpha, beta))
            if v<= alpha: return v
            beta = min(beta, v)
        return v

    def max_value(self, game, depth, alpha, beta):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        v = float("-inf")
        for m in game.get_legal_moves():
            if depth == 0:
                v = max(v, self.score(game, self))
            else:
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
            if depth == 0:
                v = self.score(game, self)
            else:
                v = self.min_value(game.forecast_move(m), depth-1, alpha, beta)
            if v > best_score:
                best_score = v
                best_move = m
            if best_score >= beta: return best_move
            alpha = max(alpha, best_score)
        return best_move

