class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.status = False

        def helper(word_index, char_row, char_col, grid):
            if word_index >= len(word):
                return
            if char_row < 0 or char_row >= len(board):
                return
            if char_col < 0 or char_col >= len(board[0]):
                return
            if board[char_row][char_col] != word[word_index]:
                return
            if board[char_row][char_col] == word[word_index]:
                if word_index == len(word) - 1:
                    self.status = True
            char = grid[char_row][char_col]
            grid[char_row][char_col] = '-'
            word_index += 1
            helper(word_index, char_row, char_col - 1, grid)
            helper(word_index, char_row - 1, char_col, grid)
            helper(word_index, char_row, char_col + 1, grid)
            helper(word_index, char_row + 1, char_col, grid)
            grid[char_row][char_col] = char

        for i in range(len(board)):
            for j in range(len(board[0])):
                helper(0, i, j, board)

        return self.status