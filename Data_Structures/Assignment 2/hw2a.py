def solveable(p_idxs, k_idx):
    # """Returns True (false) if all pawn locations can be capture by sequential knight moves"""

    # 1) Base case - is the puzzle solved?
    validMoves = valid_moves(k_idx)

    # To test the base case let's call the function
    # k_idx = (3, 3)
    # p_idxs = {(2, 1)}
    # solveable({(2, 1)}, (3, 3))

    # When k_idx = (3, 3)
    # validMoves is the following
    # validMoves = {(1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 2), (5, 4)}

    # We made
    # p_idxs = {(2, 1)}
    listOfElementsIn_p_idxs = [element for element in p_idxs]  # So, this returns [(2, 1)]
    getFirstElementIn_p_idxs = listOfElementsIn_p_idxs[0]  # So, this returns (2, 1)

    if (len(p_idxs) == 1) and (getFirstElementIn_p_idxs in validMoves):
        # 1 == 1          and  (2, 1)  in  {(1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 2), (5, 4)}
        # True            and  True
        return True

    # 2) Find all valid_moves


    # 3) Try all valid_moves
    # In my unit test
    #         k_idx = (3, 3)  # Initial knight index
    #         p_idxs = {(1, 3), (2, 1), (2, 5), (4, 2)}  # Set of pawn indices
    #         self.assertEqual(solveable(p_idxs, k_idx), True)
    # This returns FALSE, but it should be TRUE obviously
                #   0 1 2 3 4 5 6 7
                # 0 - - - - - - - -
                # 1 - - - p - - - -
                # 2 - p - - - p - -
                # 3 - - - k - - - -
                # 4 - - p - - - - -
                # 5 - - - - - - - -
                # 6 - - - - - - - -
                # 7 - - - - - - - -
    # So I will test
    # k_idx = (3, 3)
    # p_idxs = {(1, 3), (2, 1), (2, 5), (4, 2)}
    # solveable(p_idxs, k_idx)

    # validMoves would be the following since k_idx is initally set to (3, 3)
    # validMoves = {(1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 2), (5, 4)}

    # NOTE THAT SETS ARE UNORDERED SO YOU DON'T KNOW THAT ELEMENT WILL BE CHOSEN FIRST, BUT THAT SHOULDN'T MATTER HERE
    for i in validMoves:
        # p_idxs = {(1, 3), (2, 1), (2, 5), (4, 2)}
        if i in p_idxs:
            p_idxs.remove(i)
            if solveable(p_idxs, i):
                return True
            #if recursive call does not return true, put the pawn back and test other moves.
            p_idxs.append(i)
            # Your below code does not work because it does not test every possible move before returning false.
            # If the first valid knight move does not lead to a solution, you are returning the output of the recursive
            # call, which is False, before testing any of the other ones. Therefore, while you are iterating,
            # you need to test if the output is true, and if not, go back and test the other moves. You should not
            # return false at any point while iterating through possible moves.


            #p_idxsTemp = p_idxs.copy()
            #p_idxsTemp.remove(i)

            # if the variable i is the following:
            # i = (2, 1)
            # then the following return recursive call should be done

            # return solveable({(1, 3), xxx , (2, 5), (4, 2)}, (2, 1))
            # return solveable(p_idxsTemp, i)
    # 4) If nothing worked in step 3, there's no solution with the knight in this position
    return False


                # k_idx = (3, 3)
                # expected_valid_moves = {(1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 2), (5, 4)}
                # self.assertEqual(valid_moves(k_idx), expected_valid_moves)
                #  0 1 2 3 4 5 6 7
                #0 - - - - - - - -
                #1 - - x - x - - -
                #2 - x - - - x - -
                #3 - - - k - - - -
                #4 - x - - - x - -
                #5 - - x - x - - -
                #6 - - - - - - - -
                #7 - - - - - - - -
def valid_moves(k_idx):
    i = k_idx[0]  # i is row
    j = k_idx[1]  # j is column
    possibleValidMoves = [(i+2, j+1), (i+2, j-1), (i-2, j+1), (i-2, j-1),
                          (i+1, j+2), (i+1, j-2), (i-1, j+2), (i-1, j-2)]

    realValidMoves = set()
    for tup in possibleValidMoves:
        if 0 <= tup[0] <= 7 and 0 <= tup[1] <= 7:
            realValidMoves.add(tup)

    return realValidMoves
    # """Returns set of all valid moves from k_idx, assuming an 8x8 chess board"""


if __name__ == "__main__":
    print(solveable([(1, 3), (2, 1), (2, 5), (4, 2)], (3, 3)))



# TESTING STUFF HERE
# expected_valid_moves = {(1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 2), (5, 4)}
# k_idx = (3, 3)  # Initial knight index
# p_idxs = {(2, 1)}  # Set of pawn indices
#
#
# listOfElementsIn_p_idxs = [element for element in p_idxs]
# getFirstElement = listOfElementsIn_p_idxs[0]
#
# print(getFirstElement)
# print(getFirstElement in expected_valid_moves)
# # print((2, 1) in expected_valid_moves)
#
# print()
# print(solveable(p_idxs, k_idx))


# test = {(1, 2), 2, 4}
# print((1, 2) in test)
#
# # 3) Try all valid_moves
# i = {(1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 2), (5, 4)}
# j = (2, 1)
# p_idxs = {(1, 3), (2, 1), (2, 5), (4, 2), (5, 5), (6, 3)}  # Set of pawn indices
# p_idxsTemp = p_idxs.copy()
# p_idxsTemp.remove(j)
#
# print(p_idxs)
# print(p_idxsTemp)


# return solveable({(1, 3), xxx, (2, 5), (4, 2), (5, 5), (6, 3)}, (2, 1))
# return solveable(p_idxsTemp, i)

# p_idxs = {(1, 3), (2, 1), (2, 5), (4, 2)}
# print(p_idxs)
