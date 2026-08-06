class TrieNode:
    def __init__(self):
        self.children = {}
        self.flag = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = TrieNode()
        current = self.root
        for word in words:
            for char in word:
                if char not in current.children:
                    current.children[char] = TrieNode()
                current = current.children[char]
            current.flag = True
            current = self.root

        row_len = len(board)
        col_len = len(board[0])
        res = []

        def helper(current, word, row, col):
            if current.flag:
                res.append(word)
                current.flag = False
                if not current.children:
                    return
            if row < 0 or row >= row_len:
                return
            if col < 0 or col >= col_len:
                return
            if board[row][col] not in current.children:
                return
            word += board[row][col]
            #print(word)
            temp = board[row][col]
            board[row][col] = '-'
            helper(current.children[temp], word, row, col - 1)
            helper(current.children[temp], word, row + 1, col)
            helper(current.children[temp], word, row, col + 1)
            helper(current.children[temp], word, row - 1, col)
            board[row][col] = temp
        
        for i in range(row_len):
            for j in range(col_len):
                helper(self.root, "", i, j)
        return res