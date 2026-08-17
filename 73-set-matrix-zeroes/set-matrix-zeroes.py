class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=len(matrix[0])
        def markrow(i):
            for j in range(m):
                if matrix[i][j]!=0:
                    matrix[i][j]=-99
        def markcol(j):
            for i in range(n):
                if matrix[i][j]!=0:
                    matrix[i][j]=-99
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    markrow(i)
                    markcol(j)
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==-99:
                    matrix[i][j]=0
        