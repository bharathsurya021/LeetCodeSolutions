import collections


def validSudoku(board):
    rowHashSet = collections.defaultdict(set)
    colHashSet = collections.defaultdict(set)
    squareHashSet = collections.defaultdict(set)

    for row in range(9):
        for col in range(9):
            if board[row][col] == ".":
                continue
            if board[row][col] in rowHashSet[row] or board[row][
                    col] in colHashSet[col] or board[row][
                        col] in squareHashSet[(row // 3, col // 3)]:
                return False
            colHashSet[col].add(board[row][col])
            rowHashSet[row].add(board[row][col])
            squareHashSet[(row // 3, col // 3)].add(board[row][col])
    return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(validSudoku(board))
