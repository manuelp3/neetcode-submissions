class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        dic = {}
        for word in words:
            for char in word:
                dic[char] = set()
        
        for i in range(len(words) - 1):
            first = words[i]
            second = words[i + 1]
            min_length = min(len(first), len(second))
            if (first[:min_length] == second[:min_length] and
            len(first) > len(second)):
                return ""
            for j in range(min_length):
                if first[j] != second[j]:
                    dic[first[j]].add(second[j])
                    break
        
        visited = {} #dictionary -> {char : True/False}
        res = []
        def dfs(char):
            if char in visited:
                return visited[char]
            visited[char] = True
            for neighbor in dic[char]:
                if dfs(neighbor):
                    return True
            visited[char] = False
            res.append(char)
        
        for c in dic:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)