class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        def isValid(Q):
            for row1 in range(0, len(Q)):
                for row2 in range(row1+1, len(Q)):
                    col1 = Q[row1]
                    col2 = Q[row2]
                    if col1 == col2 or abs(row2-row1) == abs(col2-col1):
                        return False
            return True
        Q = []
        row, col = 0, 0
        while not (row == 0 and col == n):
            if col == n:
                row -= 1
                col = Q[row] + 1
                Q.pop(-1)
                continue
            Q.append(col)
            if row == n-1 and isValid(Q):
                result.append(Q.copy())
                col += 1
                Q.pop(-1)
            elif isValid(Q):
                row += 1
                col = 0
            else:
                col += 1
                Q.pop(-1)
        for i in range(0, len(result)):
            for j in range(0, n):
                result[i][j] = "."*result[i][j] + "Q" + '.'*(n-result[i][j]-1)

        return result
    
# metadata
# relevant-topics backtracking
# time-complexity O(N^2) 6.84%
# space-complexity O(1) 95.28%
# language python
# difficulty hard
# date 20240601