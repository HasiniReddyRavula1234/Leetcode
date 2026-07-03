class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        lst = [1,2,3,4,5,6,7,8,9]
        for i in range(9):
            col = {}
            row = {}
            for j in range(9):
                if board[i][j] != ".":
                    col[board[i][j]] = col.get(board[i][j], 0) + 1
                    if col[board[i][j]] > 1:
                        return False

                if board[j][i] != ".":
                    row[board[j][i]] = row.get(board[j][i], 0) + 1
                    if row[board[j][i]] > 1:
                        return False
        diag = {}
        for a in range(0,9,3):
                    for b in range(0,9,3):
                        diag = {}
                        for i in range(a, a + 3):
                            for j in range(b, b + 3):
                                if board[i][j] != '.':
                                    diag[board[i][j]] = diag.get(board[i][j], 0) + 1
                                    if diag[board[i][j]] > 1:
                                        return False
       
                        
        return True
        