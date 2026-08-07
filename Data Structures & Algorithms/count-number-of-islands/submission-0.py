class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        self.count = 0
        self.group = False

        def helper(row, col):
            if row < 0 or row >= rows:
                return
            if col < 0 or col >= cols:
                return
            if grid[row][col] == "0":
                return
            if not self.group:
                self.count += 1
            self.group = True
            grid[row][col] = "0"
            helper(row, col - 1)
            helper(row - 1, col)
            helper(row, col + 1)
            helper(row + 1, col)
    
        for i in range(rows):
            for j in range(cols):
                self.group = False
                helper(i, j)
        print(grid)
        return self.count