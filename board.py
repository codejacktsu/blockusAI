import numpy as np
from PIL import Image
from game_pieces import EGO_PIECES, VIL_PIECES
from moves import gen_moves_full, gen_adm_moves


class Board():
    """
    Environment
    """
    def __init__(self, size):
        self.board = np.zeros((size,size))
        self.blocks_coords = set()
        self.done = [False, False]

    def display(self):
        board_img = Image.fromarray(self.board)
        board_img.show()


class Agent():
    """
    Player
    """
    def __init__(self, pieces, player_idx):
        self.player_idx = player_idx
        self.pieces = pieces
        self.full_moves = gen_moves_full(self.pieces)
        self.diag = {(13,13)} if player_idx else {(0,0)}
        self.edge = set()
        self.color = 225 if player_idx else 100

    def move(self, board):
        if board.done[self.player_idx]:
            return None
        adm_moves = gen_adm_moves(self.full_moves, self.pieces, self.diag, self.edge, board.blocks_coords)
        # policy: random
        move_idx = np.random.choice(adm_moves)
        if adm_moves:
            move = self.full_moves[move_idx]
        else:
            board.done[self.player_idx] = True
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


# testing ground
# move = (piece_idx, piece_shape, (y,x), piece_coord, edge, diag)
game = Board(14)
p1 = Agent(EGO_PIECES, 0)
p2 = Agent(VIL_PIECES, 1)

for i in range(10):
    print(f'Move {i}:')
    p1.move(game)
    p2.move(game)
    game.display()
