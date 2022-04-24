class Solution:
    def totalNQueens(self, n):
        def backtrack(row, diagonals, antiDiagonals, colSet):
                
            # 1. If current row is greater than n, solution can be incremented by 1
            if row == n:
                return 1
           
            # -1. Check if the position is safe or not
            def safePosition():
                if col in colSet or localAntiDiagonal in antiDiagonals or localDiagonal in diagonals:
                    return False
                return True
           
            # 2. Iterate through each col of the current row
            localSolutions = 0
            for col in range(n):
                localAntiDiagonal = row+col
                localDiagonal = row-col
                if not safePosition():
                    continue
                colSet.add(col)
                antiDiagonals.add(localAntiDiagonal)
                diagonals.add(localDiagonal)

                localSolutions += backtrack(row+1, diagonals, antiDiagonals, colSet)
                
                colSet.remove(col)
                diagonals.remove(localDiagonal)
                antiDiagonals.remove(localAntiDiagonal)
                
            
            return localSolutions
        return backtrack(0, set(), set(), set())