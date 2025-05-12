def solveable(p_idxs, k_idx):
    # base case: if no more pawns left, board is solved
    if len(p_idxs) == 0:
        return True
    valid = valid_moves(k_idx)
    # try each valid move
    for move in valid:
        # only try moves that could capture a pawn
        if move in p_idxs:
            # capture pawn and recurse
            p_idxs.remove(move)
            if solveable(p_idxs, move):
                return True
            # if recursive call does not yield solution, put the pawn back on the board and try another move
            p_idxs.append(move)
    #if no recursive calls yield solution, there is no solution
    return False

def valid_moves(k_idx):
    """Returns set of all valid moves from k_idx, assuming an 8x8 chess board"""
    vert = k_idx[0]
    horiz = k_idx[1]

    #calculate all knight moves
    moves = {(vert + 2, horiz + 1), (vert + 2, horiz - 1), (vert - 2, horiz + 1), (vert - 2, horiz - 1), (vert + 1, horiz + 2), (vert + 1, horiz - 2),(vert - 1, horiz + 2),(vert - 1, horiz - 2)}
    valid = set()
    #take out any invalid moves
    for index in moves:
        if index[0] < 0 or index[0] > 7 or index[1] < 0 or index[1] > 7:
            continue
        valid.add(index)
    return valid

