class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for string in strs:
            key = [0] * 26
            for char in string:
                value = ord(char) - ord('a')
                key[value] += 1
            if tuple(key) in dic:
                dic[tuple(key)].append(string)
            else:
                dic[tuple(key)] = [string]
        res = []
        for key in dic:
            res.append(dic[key])
        return res
        