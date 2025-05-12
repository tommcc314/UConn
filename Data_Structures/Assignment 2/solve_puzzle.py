def solve_puzzle(board):
    #goal is the last index of the list
    goal = len(board) - 1
    def test_puzzle(board, index, visited): # index is the current spot, visited is a list of past spots
        #base case: if on the goal index, board is solved
        if index == goal:
            return True

        #if I've visited the exact same spot, look elsewhere
        if index in visited:
            return False
        #test clockwise and counterclockwise directions
        clockwise = (index + board[index]) % len(board)
        counterclockwise = (index - board[index]) % len(board)
        visited.append(index)
        return test_puzzle(board, clockwise, visited) or test_puzzle(board, counterclockwise, visited)
    return test_puzzle(board, 0, [])
