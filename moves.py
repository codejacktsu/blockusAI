import numpy as np
from PIL import Image
from game_pieces import EGO_PIECES


def gen_moves_full(pieces):
    """
    Generate complete move dict
    :param pieces: list of pieces
    :return: dict[move_idx]: (piece_idx, piece_shape, (y,x), piece_coord, edge, diag)
    """
    move_list_full = {}
    move_count = 0
    # move_list_full[move_count] = (None, None, None, None, None, None)
    for idx, piece in enumerate(pieces):
        for x in range(14-piece.width()+1):
            for y in range(14-piece.height()+1):
                move_count += 1
                blocks = piece.gen_coord((y, x))
                edge, diag = gen_edge_diag(blocks)
                move_list_full[move_count] = (idx, piece.shape, (y, x), blocks, edge, diag)
        if piece.rot_sym > 1:
            for _ in range(piece.rot_sym - 1):
                piece.rotate()
                for x in range(14 - piece.width() + 1):
                    for y in range(14 - piece.height() + 1):
                        move_count += 1
                        blocks = piece.gen_coord((y, x))
                        edge, diag = gen_edge_diag(blocks)
                        move_list_full[move_count] = (idx, piece.shape, (y, x), blocks, edge, diag)
        if not piece.flip_sym:
            piece.flip()
            for _ in range(piece.rot_sym):
                piece.rotate()
                for x in range(14 - piece.width() + 1):
                    for y in range(14 - piece.height() + 1):
                        move_count += 1
                        blocks = piece.gen_coord((y, x))
                        edge, diag = gen_edge_diag(blocks)
                        move_list_full[move_count] = (idx, piece.shape, (y, x), blocks, edge, diag)
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
    return bool(set(move_coord) & req_list)


def check_restrict(move_coord, restrict_list):
    """
    Check move eligibility: if move candidate not on edge (restrict) or existing blocks (restrict)
    :param move_coord: list
    :param edge_list: list
    :return: bool - True: eligible, False: ineligible
    """
    return not bool(set(move_coord) & restrict_list)


def gen_adm_moves(player_moves_full, player_pieces, diag, edge, exist_blocks):
    """
    Generate admissible moves by player
    :param player_moves_full: dict
    :param player_pieces: list
    :param diag: set
    :param edge: set
    :param exist_blocks: set
    :return: int list of move_idx
    """
    adm_moves = []
    for idx in range(1, len(player_moves_full)+1):
        move = player_moves_full[idx]
        if check_pieces(move[0], player_pieces) and check_require(move[3], diag) and check_restrict(move[3], edge) and check_restrict(move[3], exist_blocks):
            adm_moves.append(idx)
    return adm_moves


def gen_edge_diag(blocks):
    edge = set()
    diag = set()
    for coord in blocks:
        y, x = coord[0], coord[1]
        tl, top, tr = (y-1, x-1), (y-1, x), (y-1, x+1)
        left, right = (y, x-1), (y, x+1)
        bl, bot, br = (y+1, x-1), (y+1, x), (y+1, x+1)
        tmp_edge = [top, left, right, bot]
        tmp_diag = [tl, tr, bl, br]
        for pt in tmp_edge:
            if pt in blocks:
                continue
            elif 0 <= pt[0] <= 13 and 0 <= pt[1] <= 13:
                edge.add(pt)
                diag.discard(pt)
        for pt in tmp_diag:
            if pt in blocks or pt in edge:
                continue
            elif 0 <= pt[0] <= 13 and 0 <= pt[1] <= 13:
                diag.add(pt)
    return edge, diag


# move = piece, rotate, orient, coord
ego_moves_full = gen_moves_full(EGO_PIECES)


# test ground
# rand_idx = np.random.randint(0,16217)
# move = move_list_full[rand_idx]
# print(move[0], move[1])
# make_move(game, piece, 0, 1, 5, 5)

