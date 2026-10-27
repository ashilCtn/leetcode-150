class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        sqrs = defaultdict(list)

        ROW = len(board)
        COL = len(board[0])

        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in sqrs[(i // 3, j // 3)]:
                    return False
                else:
                    rows[i].append(board[i][j])
                    cols[j].append(board[i][j])
                    sqrs[(i // 3, j // 3)].append(board[i][j])
        return True
        
        