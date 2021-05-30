import numpy as np
from PIL import Image
from game_pieces import EGO_PIECES
from board import Board


def make_move(board, piece, rot, flip, x, y):
    """
    Make a move
    :param board: board object
    :param piece: piece object
    :param rot: int rotation
    :param flip: bool flip
    :param x: TL X coord
    :param y: TL Y coord
    :return: none
    """
    if rot:
        for _ in range(rot):
            piece.rotate()
    if flip:
        piece.flip()
    piece_img = Image.fromarray(piece.shape)
    board_img = Image.fromarray(board.board)
    board_img.paste(piece_img, (x, y))
    # remove piece from list
    board_img.show()


def gen_moves_full(pieces):
    """
    Generate complete move dict
    :param pieces: list of pieces
    :return: dict
    """
    move_list_full = {}
    move_count = 0
    for idx, piece in enumerate(pieces):
        for x in range(14-piece.width()+1):
            for y in range(14-piece.height()+1):
                move_count += 1
                move_list_full[move_count] = (idx, piece.shape, (y, x), piece.gen_coord((y, x)))
        if not piece.rot_sym:
            for _ in range(3):
                piece.rotate()
                for x in range(14 - piece.width() + 1):
                    for y in range(14 - piece.height() + 1):
                        move_count += 1
                        move_list_full[move_count] = (idx, piece.shape, (y, x), piece.gen_coord((y, x)))
        if not piece.flip_sym:
            piece.flip()
            for _ in range(4):
                piece.rotate()
                for x in range(14 - piece.width() + 1):
                    for y in range(14 - piece.height() + 1):
                        move_count += 1
                        move_list_full[move_count] = (idx, piece.shape, (y, x), piece.gen_coord((y, x)))
    return move_list_full


# move = piece, rotate, orient, coord
ego_moves_full = gen_moves_full(EGO_PIECES)


# test ground
# rand_idx = np.random.randint(0,16217)
# move = move_list_full[rand_idx]
# print(move[0], move[1])
# make_move(game, piece, 0, 1, 5, 5)

