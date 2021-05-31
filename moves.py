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
        if piece.rot_sym > 1:
            for _ in range(piece.rot_sym - 1):
                piece.rotate()
                for x in range(14 - piece.width() + 1):
                    for y in range(14 - piece.height() + 1):
                        move_count += 1
                        move_list_full[move_count] = (idx, piece.shape, (y, x), piece.gen_coord((y, x)))
        if not piece.flip_sym:
            piece.flip()
            for _ in range(piece.rot_sym):
                piece.rotate()
                for x in range(14 - piece.width() + 1):
                    for y in range(14 - piece.height() + 1):
                        move_count += 1
                        move_list_full[move_count] = (idx, piece.shape, (y, x), piece.gen_coord((y, x)))
    return move_list_full


def check_pieces(piece_idx, pieces):
    """
    Check move eligibility: if piece is available to play
    :param piece_idx: int
    :param pieces: list
    :return: bool True: eligible, False: ineligible
    """
    return pieces[piece_idx].available


def check_require(move_coord, req_list):
    """
    Check move eligibility: if move candidate on diagonal (required)
    :param move_coord: list
    :param diag_list: list
    :return: bool - True: eligible, False: ineligible
    """
    return bool(set(move_coord) & set(req_list))


def check_restrict(move_coord, restrict_list):
    """
    Check move eligibility: if move candidate not on edge (restrict) or existing blocks (restrict)
    :param move_coord: list
    :param edge_list: list
    :return: bool - True: eligible, False: ineligible
    """
    return not bool(set(move_coord) & set(restrict_list))


def gen_adm_moves(player_moves_full, player_pieces, diag, edge, exist_blocks):
    """
    Generate admissible moves by player
    :param player_moves_full: dict
    :param player_pieces: list
    :param diag: list
    :param edge: list
    :param exist_blocks: list
    :return: int list of move_idx
    """
    adm_moves = []
    for idx in range(1, len(player_moves_full)+1):
        move = player_moves_full[idx]
        if check_pieces(move[0], player_pieces) and check_require(move[3], diag) and check_restrict(move[3], edge) and check_restrict(move[3], exist_blocks):
            adm_moves.append(idx)
    return adm_moves


# move = piece, rotate, orient, coord
ego_moves_full = gen_moves_full(EGO_PIECES)


# test ground
# rand_idx = np.random.randint(0,16217)
# move = move_list_full[rand_idx]
# print(move[0], move[1])
# make_move(game, piece, 0, 1, 5, 5)

