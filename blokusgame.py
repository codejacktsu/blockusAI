import numpy as np

"""
The state of the game is a numpy array
* Are values are either 0 or 1
* Shape [SIZE, SIZE, 1]
0 - Blank
1~21 - Black pieces
231~251 - White pieces
2 - Turn (0 - black, 1 - white)
3 - Previous move was a pass
4 - Game over
"""

size = 3

def init_state():
    state = np.zeros((size,size,1))
    return state


def next_state(state, action1d):
    state = np.copy(state)


def free_corners(state, player):
    corners = [0, 13, 182,195]

def cell_id(pix_id, size):
    """
    identify cell's category
    :param pix_id:
    :param size:
    :return: string cell
    """
    corner2 = size-1
    corner3 = size*corner2
    corner4 = size*size-1
    if pix_id == 0:
        return "corner1"
    elif pix_id == corner2:
        return "corner2"
    elif pix_id == corner3:
        return "corner3"
    elif pix_id == corner4:
        return "corner4"
    elif 0 < pix_id < corner2:
        return "top"
    elif corner3 < pix_id < corner4:
        return "bot"
    elif pix_id % size == 0:
        return "left"
    elif (pix_id-corner2) % size == 0:
        return "right"
    else:
        return "middle"


def cell_border(pix_id, state, player, size):
    if player == "black":
        min_thresh, max_thresh = 1, 21
    else:
        min_thresh, max_thresh = 231, 251
    category = cell_id(pix_id, size)
    if category == "corner1":
        if check_diag(pix_id, state, size, min_thresh, max_thresh, 3):
            pass


def check_diag(pix_id, state, size, low, high, diag):
    """
    check diagonal cell's move eligibility - order 1: TL 2: TR 3: BL 4: BR
    :param pix_id:
    :param state:
    :param size:
    :param low:
    :param high:
    :return: bool
    """
    if diag == 1:
        diag, side1, side2 = pix_id - size - 1, pix_id - size, pix_id - 1
    elif diag == 2:
        diag, side1, side2 = pix_id - size + 1, pix_id - size, pix_id + 1
    elif diag == 3:
        diag, side1, side2 = pix_id + size - 1, pix_id + size, pix_id - 1
    elif diag == 4:
        diag, side1, side2 = pix_id - size + 1, pix_id + size, pix_id + 1

    if state[diag] == 0 \
            and low > state[side1] and high < state[side1] \
            and low > state[side2] and high < state[side2]:
        return True
    else:
        return False


game = init_state()

for idx, pixel in enumerate(game.flatten()):
    print(idx)
    check_corners(idx, 1, 1, 3)

