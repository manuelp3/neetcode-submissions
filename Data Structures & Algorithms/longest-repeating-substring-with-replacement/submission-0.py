class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, end = 0, 0
        res = 0
        count = {}
        
        while (end < len(s)):
            count[s[end]] = 1 + count.get(s[end], 0)
            if (end - start + 1 - max(count.values()) > k):
                count[s[start]] -= 1
                start+=1    
            res = max(res, end - start + 1)
            end+=1
        return res