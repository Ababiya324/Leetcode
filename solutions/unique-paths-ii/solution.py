class Solution:
    def uniquePathsWithObstacles(self, grid):
        m, n = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return 0

        def comb(a, b):
            if b < 0 or b > a:
                return 0
            b = min(b, a - b)
            num = 1
            for i in range(b):
                num = num * (a - i) // (i + 1)
            return num

        def paths(r1, c1, r2, c2):
            if r2 < r1 or c2 < c1:
                return 0
            dr, dc = r2 - r1, c2 - c1
            return comb(dr + dc, dr)

        obstacles = [(r, c) for r in range(m) for c in range(n) if grid[r][c] == 1]
        obstacles.sort()

        dp = [0] * len(obstacles)
        for i, (ri, ci) in enumerate(obstacles):
            dp[i] = paths(0, 0, ri, ci)
            for j in range(i):
                rj, cj = obstacles[j]
                if rj <= ri and cj <= ci:
                    dp[i] -= dp[j] * paths(rj, cj, ri, ci)

        total = paths(0, 0, m - 1, n - 1)
        bad = sum(dp[i] * paths(ri, ci, m - 1, n - 1)
                  for i, (ri, ci) in enumerate(obstacles))
        return total - bad