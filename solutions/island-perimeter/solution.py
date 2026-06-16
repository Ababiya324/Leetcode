class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        
        """
        v = 0
        h = 0
        for i in range(len(grid)):
            m = False
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    if j == 0 or grid[i][j-1] == 0:
                        v += 1
                    if j == len(grid[i]) - 1 or grid[i][j+1] == 0:
                        v += 1
                    if i == 0 or grid[i-1][j] == 0:
                        h += 1
                    if i == len(grid) - 1 or grid[i+1][j] == 0:
                        h += 1
        return v + h



        