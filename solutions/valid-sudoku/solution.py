class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        for i in range(9):
            s = []
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in s:
                    return False
                s.append(board[i][j])
                
        for j in range(9):
            s = []
            for i in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in s:
                    return False
                s.append(board[i][j])
                
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                s = []
                for a in range(i, i + 3):
                    for b in range(j, j + 3):
                        if board[a][b] == ".":
                            continue
                        if board[a][b] in s:
                            return False
                        s.append(board[a][b])        
        return True #slow
