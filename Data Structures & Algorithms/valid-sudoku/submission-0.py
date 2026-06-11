class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Let's check horizontally first
        for i in range(len(board)):
            seen = set()
            for j in range(len(board)):
                if board[i][j] != ".": 
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
                
        # Let's check vertically now
        for i in range(len(board)):
            seen = set()
            for j in range(len(board)):
                if board[j][i] != ".": 
                    if board[j][i] in seen:
                        return False   
                    seen.add(board[j][i])
                

        # Let's check 3x3 subboxes:
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] != ".":
                        if board[row][col] in seen:
                            return False
                        seen.add(board[row][col])
        return True
