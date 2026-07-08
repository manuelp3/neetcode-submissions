class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        minLength = float("inf")
        countT = {}
        for char in t:
            countT[char] = countT.get(char, 0) + 1
        
        countS = {}
        has, need = len(countT), 0
        start = 0

        for end in range(len(s)):
            countS[s[end]] = countS.get(s[end], 0) + 1
            if (countS[s[end]] == countT.get(s[end], 0)):
                need += 1
            while has == need and start < len(s):
                if (end - start + 1 < minLength):
                    res = s[start:end + 1]
                    minLength = end - start + 1
                countS[s[start]] -= 1
                if (countS[s[start]] < countT.get(s[start], 0)):
                    need -= 1
                start += 1
        return res