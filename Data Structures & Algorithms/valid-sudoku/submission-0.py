class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        counts = defaultdict(int)
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    counts[board[i][j]]+=1
                    if counts[board[i][j]] > 1:
                        return False
            counts = defaultdict(int)
        for i in range(9):
            for j in range(9):
                if board[j][i] != ".":
                    counts[board[j][i]]+=1
                    if counts[board[j][i]] > 1:
                        return False
            counts = defaultdict(int)
        for r in range(0,9,3):
            for c in range(0,9,3):
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        if board[i][j] != ".":
                            counts[board[i][j]] += 1
                            if counts[board[i][j]] > 1:
                                return False
                counts = defaultdict(int)
        return True





