import cv2
import numpy as np


class Piece():
    '''
    The Fundamenal Game Object
    '''

    def __init__(self, shape, flip_sym=False, rot_sym=False):
        self.initial_shape = shape
        self.shape = shape
        self.flip_sym = flip_sym
        self.rot_sym = rot_sym
        self.available = True
        self.moves = {}

    def height(self):
        return len(self.shape)

    def width(self):
        return len(self.shape[0])

    def reset_shape(self):
        self.shape = [row[:] for row in self.initial_shape]

    def rotate(self):
        self.shape = np.rot90(self.shape)

    def set_color(self, color):
        """
        set pieces color
        :param color: ego - 255, vil - 125
        """
        self.initial_shape *= color
        # self.shape *= color

    def flip(self):
        self.shape = np.flip(self.shape)

    def gen_moves(self):
        pass


# 4 ways
LONG_L = Piece(np.array(
    [[1, 1, 1],
     [1, 0, 0],
     [1, 0, 0]],
    dtype=np.uint8),
    flip_sym=True
)

LANKY_L = Piece(np.array(
    [[1, 1, 1, 1],
     [1, 0, 0, 0]],
    dtype=np.uint8
))

SMALL_T = Piece(np.array(
    [[0, 1, 0],
     [1, 1, 1]],
    dtype=np.uint8),
    flip_sym=True
)

BACKPACK_L = Piece(np.array(
    [[0, 1, 0],
     [1, 1, 1],
     [1, 0, 0]],
    dtype=np.uint8
))

THUMB = Piece(np.array(
    [[1, 1],
     [1, 1],
     [0, 1]],
    dtype=np.uint8
))

SQUARE = Piece(np.array(
    [[1, 1],
     [1, 1]],
    dtype=np.uint8),
    flip_sym=True,
    rot_sym=True
)

THREE_LINE = Piece(np.array(
    [[1],
     [1],
     [1]],
    dtype=np.uint8),
    flip_sym=True
)

HALBERD = Piece(np.array(
    [[0, 1],
     [1, 1],
     [0, 1],
     [0, 1]],
    dtype=np.uint8
))

PLUS = Piece(np.array(
    [[0, 1, 0],
     [1, 1, 1],
     [0, 1, 0]],
    dtype=np.uint8),
    flip_sym=True,
    rot_sym=True
)

TWO_LINE = Piece(np.array(
    [[1],
     [1]],
    dtype=np.uint8),
    flip_sym=True
)

FOUR_LINE = Piece(np.array(
    [[1],
     [1],
     [1],
     [1]],
    dtype=np.uint8),
    flip_sym=True
)

T = Piece(np.array(
    [[1, 0, 0],
     [1, 1, 1],
     [1, 0, 0]],
    dtype=np.uint8),
    flip_sym=True
)

WAVE = Piece(np.array(
    [[1, 0, 0],
     [1, 1, 0],
     [0, 1, 1]],
    dtype=np.uint8),
    flip_sym=True
)

L = Piece(np.array(
    [[1, 1],
     [0, 1],
     [0, 1]],
    dtype=np.uint8
))

O = Piece(np.array(
    [[1]],
    dtype=np.uint8),
    flip_sym=True,
    rot_sym=True
)

ELBOW = Piece(np.array(
    [[1, 1],
     [1, 0]],
    dtype=np.uint8),
    flip_sym=True
)

SNAKE = Piece(np.array(
    [[0, 1],
     [1, 1],
     [1, 0],
     [1, 0]],
    dtype=np.uint8
))

Z = Piece(np.array(
    [[0, 1],
     [1, 1],
     [1, 0]],
    dtype=np.uint8
))

S = Piece(np.array(
    [[0, 1, 1],
     [0, 1, 0],
     [1, 1, 0]],
    dtype=np.uint8
))

U = Piece(np.array(
    [[1, 0, 1],
     [1, 1, 1]],
    dtype=np.uint8),
    flip_sym=True
)

FIVE_LINE = Piece(np.array(
    [[1],
     [1],
     [1],
     [1],
     [1]],
    dtype=np.uint8),
    flip_sym=True
)

EGO_PIECES = [
    LONG_L,
    LANKY_L,
    SMALL_T,
    BACKPACK_L,
    THUMB,
    SQUARE,
    THREE_LINE,
    HALBERD,
    PLUS,
    TWO_LINE,
    FOUR_LINE,
    T,
    WAVE,
    L,
    O,
    ELBOW,
    SNAKE,
    Z,
    S,
    U,
    FIVE_LINE
]

VIL_PIECES = EGO_PIECES.copy()

for piece in EGO_PIECES:
    piece.set_color(225)

for piece in VIL_PIECES:
    piece.set_color(100)


# TESTING GROUND
# img = cv2.resize(WAVE.shape, (300,300))
# cv2.imshow("test", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()