class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numrows = len(grid)
        numcols = len(grid[0])

        def dfs(row, col):
            if row < 0 or row >= numrows:
                return
            if col < 0 or col >= numcols:
                return
            if grid[row][col] == "0":
                return
            grid[row][col] = "0"
            dfs(row, col - 1)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row + 1, col)
        
        res = 0
        for i in range(numrows):
            for j in range(numcols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        return res