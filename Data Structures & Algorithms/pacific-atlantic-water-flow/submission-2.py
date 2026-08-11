class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row_len = len(heights)
        col_len = len(heights[0])
        pac = set()
        atl = set()

        def dfs(row, col, last, visited):
            if (row, col) in visited or row < 0 or row == row_len or col < 0 or col == col_len or heights[row][col] in visited or heights[row][col] < last:
                return
            visited.add((row, col))
            dfs(row - 1, col, heights[row][col], visited)
            dfs(row + 1, col, heights[row][col], visited)
            dfs(row, col - 1, heights[row][col], visited)
            dfs(row, col + 1, heights[row][col], visited)

        for c in range(col_len):
            dfs(0, c, heights[0][c], pac)
            dfs(row_len - 1, c, heights[row_len - 1][c], atl)
        
        for r in range(row_len):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, col_len - 1, heights[r][col_len - 1], atl)
        
        # print(pac)
        # print(atl)

        res = []

        for i in range(row_len):
            for j in range(col_len):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        return res
        