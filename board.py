import numpy as np


class Board():
    def __init__(self, size):
        self.board = np.zeros((size,size))


# testing ground
# game = Board(14)
#
# print(game.board)