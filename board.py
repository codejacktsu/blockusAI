import numpy as np
from PIL import Image
from copy import deepcopy
import time

from game_pieces import EGO_PIECES, VIL_PIECES
from moves import gen_moves_full, gen_adm_moves


class Board():
    """
    Environment
    """
    def __init__(self, size):
        self.size = size
        self.board = np.zeros((self.size,self.size))
        self.blocks_coords = set()
        self.done = [False, False]

    def display(self):
        board_img = Image.fromarray(self.board)
        board_img.show()

    def reset(self):
        self.board = np.zeros((self.size,self.size))
        self.blocks_coords = set()
        self.done = [False, False]


class Agent():
    """
    Player X
    """
    def __init__(self, pieces, player_idx):
        self.player_idx = player_idx
        self.pieces = deepcopy(pieces)
        self.full_moves = gen_moves_full(self.pieces)
        self.diag = {(13,13)} if player_idx else {(0,0)}
        self.edge = set()
        self.color = 225 if player_idx else 100
        self.reward = 0 # 89 total points, special rule +15 for all/ +5 for playing 1x1 last
        self.done = False

    def move(self, board):
        if board.done[self.player_idx]:
            return None
        adm_moves = gen_adm_moves(self.full_moves, self.pieces, self.diag, self.edge, board.blocks_coords)
        # TODO: RL Policy - Current random
        if adm_moves:
            move_idx = np.random.choice(adm_moves)
            move = self.full_moves[move_idx]
        else:
            board.done[self.player_idx] = True
            self.gen_reward()
            return None

        # remove from available pieces
        self.pieces[move[0]].available = False
        # add to board + block_coord
        for coord in move[3]:
            board.board[coord[0]][coord[1]] = self.color        # add to board.board
            board.blocks_coords.add(coord)                      # add to board.block_coord
            self.diag.discard(coord)                            # update diag
        # update edge/diag
        self.edge = set.union(self.edge, move[4])
        self.diag = set.union(self.diag, move[5]).difference(self.edge).difference(board.blocks_coords)

        # gen reward
        print(f'{self.player_idx}: {len(adm_moves)}')

    def gen_reward(self):
        points = 100 # 89 total
        for piece in self.pieces:
            if piece.available:
                points -= piece.points
        self.reward = points
        return self.reward


def run_a_game():
    """
    dummy quick game result
    :return:
    """
    at0 = time.time()
    game = Board(14)
    p1 = Agent(EGO_PIECES, 0)
    p2 = Agent(VIL_PIECES, 1)
    at1 = round(time.time()-at0, 2)

    bt0 = time.time()
    for i in range(20):
        if game.done[0] and game.done[1]:
            print(f'End!')
            bt1 = round(time.time() - bt0, 2)
            print(f'P1 Score: {p1.reward} | P2 Score: {p2.reward} in {i} turns & {bt1} seconds')
            print(f'Game init {at1} seconds & Game run {bt1} seconds')
            game.display()
            break
        print(f'Move {i}:')
        p1.move(game)
        p2.move(game)


# testing ground
# move = (piece_idx, piece_shape, (y,x), piece_coord, edge, diag)
# game = Board(14)
# p1 = Agent(EGO_PIECES, 0)
# p2 = Agent(VIL_PIECES, 1)

# run_a_game()
