import cv2
import numpy as np


class Piece():
    '''
    The Fundamenal Game Object
    '''

    def __init__(self, shape):
        self.initial_shape = shape
        self.shape = shape
        self.grid_x, self.grid_y = 0, 0

    def height(self):
        return len(self.shape)

    def width(self):
        return len(self.shape[0])

    # Horizontal board position to terminal coordinate transformation
    def grid_to_xpos(self):
        return 2*self.grid_x + self.board_left

    # Vertical board position to terminal coordinate transformation
    def grid_to_ypos(self):
        return self.grid_y + self.board_top

    def reset_shape(self):
        self.shape = [row[:] for row in self.initial_shape]

    def rotate(self):
        self.shape = np.rot90(self.shape)

    def set_color(self, color):
        """
        set pieces color
        :param color: ego - 255, vil - 125
        """
        self.initial_shape = self.initial_shape*color
        self.shape = self.shape*color

    def flip(self):
        self.shape = np.flip(self.shape)


LONG_L = Piece(np.array(
    [[1, 1, 1],
     [1, 0, 0],
     [1, 0, 0]],
    dtype=np.uint8
))

LANKY_L = Piece(np.array(
    [[1, 1, 1, 1],
     [1, 0, 0, 0]],
    dtype=np.uint8
))

SMALL_T = Piece(np.array(
    [[0, 1, 0],
     [1, 1, 1]],
    dtype=np.uint8
))

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
    dtype=np.uint8
))

THREE_LINE = Piece(np.array(
    [[1],
     [1],
     [1]],
    dtype=np.uint8
))

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
    dtype=np.uint8
))

TWO_LINE = Piece(np.array(
    [[1],
     [1]],
    dtype=np.uint8
))

FOUR_LINE = Piece(np.array(
    [[1],
     [1],
     [1],
     [1]],
    dtype=np.uint8
))

T = Piece(np.array(
    [[1, 0, 0],
     [1, 1, 1],
     [1, 0, 0]],
    dtype=np.uint8
))

WAVE = Piece(np.array(
    [[1, 0, 0],
     [1, 1, 0],
     [0, 1, 1]],
    dtype=np.uint8
))

L = Piece(np.array(
    [[1, 1],
     [0, 1],
     [0, 1]],
    dtype=np.uint8
))

O = Piece(np.array(
    [[1]],
    dtype=np.uint8
))

ELBOW = Piece(np.array(
    [[1, 1],
     [1, 0]],
    dtype=np.uint8
))

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
    dtype=np.uint8
))

FIVE_LINE = Piece(np.array(
    [[1],
     [1],
     [1],
     [1],
     [1]],
    dtype=np.uint8
))

EGO_PIECES = [
    LONG_L,
    LANKY_L,
    SMALL_T,
    THUMB,
    SQUARE,
    BACKPACK_L,
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

for pieces in EGO_PIECES:
    pieces.set_color(255)

for pieces in VIL_PIECES:
    pieces.set_color(125)

# TESTING GROUND
# img = cv2.resize(WAVE.shape, (300,300))
# cv2.imshow("test", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()