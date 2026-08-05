class TrieNode():
    def __init__(self):
        self.children = {}
        self.flag = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for i in range(len(word)):
            char = word[i]
            if char in current.children.keys():
                current = current.children[char]
            else:
                current.children[char] = TrieNode()
                current = current.children[char]
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
            if char not in current.children.keys():
                return False
            current = current.children[char]    
        return True
        