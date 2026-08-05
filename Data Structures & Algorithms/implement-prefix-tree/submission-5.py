class TreeNode():
    def __init__(self, char='',children=None,flag=False):
        self.char = char
        self.children = {} if children is None else children
        self.flag = flag

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        current = self.root
        for i in range(len(word)):
            char = word[i]
            if char in current.children.keys():
                current = current.children[char]
            else:
                current.children[char] = TreeNode(char)
                current = current.children[char]
            if i == len(word) - 1:
                current.flag = True


    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current.children.keys():
                return False
            current = current.children[char]
        return current.flag

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char in current.children.keys():
                current = current.children[char]
            else:
                return False
        return True
        