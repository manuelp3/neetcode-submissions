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

    def helper(self, index, word, current):
        if index == len(word):
            return current.flag
        char = word[index]
        if char == ".":
            for node in current.children.values():
                if self.helper(index + 1, word, node):
                    return True
            return False
        else:
            if word[index] not in current.children:
                return False
            current = current.children[char]
            return self.helper(index + 1, word, current)

    def search(self, word: str) -> bool:
        return self.helper(0, word, self.root)
