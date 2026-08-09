class TrieNode:
    def __init__(self):
        self.children = {}
        self.flag = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.flag = True

    def search(self, word: str) -> bool:
        length = len(word)
        def helper(index, current):
            if index == length:
                return current.flag
            char = word[index]
            if char == ".":
                for node in current.children.values():
                    if helper(index + 1, node):
                        return True
                return False
            else:
                if word[index] not in current.children:
                    return False
                current = current.children[char]
                return helper(index + 1, current)
        return helper(0, self.root)
