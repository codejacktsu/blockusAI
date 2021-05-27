from game_pieces import EGO_PIECES


# move = coord, piece, rotate, orient
ego_moves = {}
move_count = 0

for piece in EGO_PIECES:
    move_count += 1
    if not piece.rot_sym:
        for _ in range(3):
            piece.rotate()
            move_count += 1

    if not piece.flip_sym:
        piece.flip()
        move_count += 1
        for _ in range(3):
            piece.rotate()
            move_count += 1


print(move_count)

