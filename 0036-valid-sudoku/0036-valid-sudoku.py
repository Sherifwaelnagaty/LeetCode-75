class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for i in range(len(board)):
            stack = ["1","2","3","4","5","6","7","8","9"]
            for j in range(len(board[i])):
                if board[i][j] in stack:
                    stack.remove(board[i][j])
                elif board[i][j] == ".":
                    continue
                else:
                    return False
        
        # Check columns
        for j in range(len(board[0])):
            stack = ["1","2","3","4","5","6","7","8","9"]
            for i in range(len(board)):
                if board[i][j] in stack:
                    stack.remove(board[i][j])
                elif board[i][j] == ".":
                    continue
                else:
                    return False

        # Check 3x3 subgrids
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                stack = ["1","2","3","4","5","6","7","8","9"]
                for k in range(3):
                    for l in range(3):
                        if board[i + k][j + l] in stack:
                            stack.remove(board[i + k][j + l])
                        elif board[i + k][j + l] == ".":
                            continue
                        else:
                            return False

        return True

        