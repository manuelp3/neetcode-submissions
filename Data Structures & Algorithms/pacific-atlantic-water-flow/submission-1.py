class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row_len = len(heights)
        col_len = len(heights[0])
        res = []
        def pacific(row, col, last, visited):
            if row < 0 or col < 0:
                return True
            if row >= row_len or col >= col_len:
                return False
            if (row, col) in visited:
                return False
            if heights[row][col] > last:
                return False
            visited.add((row, col))
            return pacific(row, col - 1, heights[row][col], visited) or pacific(row - 1, col, heights[row][col], visited) or pacific(row, col + 1, heights[row][col], visited) or pacific(row + 1, col, heights[row][col], visited)

        def atlantic(row, col, last, visited):
            if row >= row_len or col >= col_len:
                return True
            if row < 0 or col < 0:
                return False
            if (row, col) in visited:
                return False
            if heights[row][col] > last:
                return False
            visited.add((row, col))
            return atlantic(row, col - 1, heights[row][col], visited) or atlantic(row - 1, col, heights[row][col], visited) or atlantic(row, col + 1, heights[row][col], visited) or atlantic(row + 1, col, heights[row][col], visited)

        for i in range(row_len):
            for j in range(col_len):
                if pacific(i, j, heights[i][j], set()) and atlantic(i, j, heights[i][j], set()):
                    res.append([i,j])
                    print(res)
        return res