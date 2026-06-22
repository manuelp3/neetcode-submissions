class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}

        for i in range(0, len(s)):
            if s[i] in dict1:
                dict1[s[i]] = dict1[s[i]] + 1
            else:
                dict1[s[i]] = 1
        
        for i in range(0, len(t)):
            if t[i] in dict2:
                dict2[t[i]] = dict2[t[i]] + 1
            else:
                dict2[t[i]] = 1

        return dict1 == dict2