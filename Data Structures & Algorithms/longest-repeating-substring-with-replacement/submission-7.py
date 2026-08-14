class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        smap = {}
        maxLength = 1
        start, end = 0, 1
        smap[s[start]] = 1
        high = 0
        while end < len(s):
            smap[s[end]] = smap.get(s[end], 0) + 1
            high = max(high, smap[s[end]])
            if (end - start + 1 - high > k):
                smap[s[start]] -= 1
                start += 1
            length = end - start + 1
            maxLength = max(maxLength, length)
            end += 1
        return maxLength