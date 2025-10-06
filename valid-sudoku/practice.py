import collections
from typing import List

class Solution:
  def isValidSudoku(self, board: List[List[int]]) -> bool:
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    squares = collections.defaultdict(set) # key = (r // 3, c // 3)

    for r in range(len(board)):
      for c in range(len(board[0])):
        # skip empty values (".")
        if board[r][c] == ".":
          continue
        
        # check if value is duplicated
        if (board[r][c] in rows[r] or
            board[r][c] in cols[c] or
            board[r][c] in squares[(r // 3, c // 3)]):
          return False

        # update all 3 hash sets
        rows[r].add(board[r][c])
        cols[c].add(board[r][c])
        squares[((r // 3, c // 3))].add(board[r][c])

    print(rows)
    print(cols)
    print(squares)

    return True


if __name__ == "__main__":
  s = Solution()
  board = [["5","3",".",".","7",".",".",".","."],
           ["6",".",".","1","9","5",".",".","."],
           [".","9","8",".",".",".",".","6","."],
           ["8",".",".",".","6",".",".",".","3"],
           ["4",".",".","8",".","3",".",".","1"],
           ["7",".",".",".","2",".",".",".","6"],
           [".","6",".",".",".",".","2","8","."],
           [".",".",".","4","1","9",".",".","5"],
           [".",".",".",".","8",".",".","7","9"]]
  print(s.isValidSudoku(board))
