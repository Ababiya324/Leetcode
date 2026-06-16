class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        pending = {}  
        for i in range(n):
            for j in range(n):
                src = pending.pop((i, j), matrix[i][j]) 
                di, dj = j, n - 1 - i
                pending[(di, dj)] = matrix[di][dj]       
                matrix[di][dj] = src