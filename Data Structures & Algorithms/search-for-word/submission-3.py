class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.status = False
        rows, cols = len(board), len(board[0])

        def helper(word_index, row, col):
            if row < 0 or row == rows:
                return
            if col < 0 or col == cols:
                return
            if board[row][col] != word[word_index]:
                return
            if board[row][col] == word[word_index]:
                if word_index == len(word) - 1:
                    self.status = True
                    return
            word_index += 1
            char = board[row][col]
            board[row][col] = '-'
            helper(word_index, row, col - 1)
            helper(word_index, row - 1, col)
            helper(word_index, row, col + 1)
            helper(word_index, row + 1, col)
            board[row][col] = char

        for i in range(len(board)):
            for j in range(len(board[0])):
                helper(0, i, j)
        
        return self.status