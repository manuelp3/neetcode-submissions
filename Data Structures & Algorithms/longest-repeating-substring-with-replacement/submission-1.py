class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        start, end = 0, 0
        res = 0

        while (end < len(s)):
            freq[s[end]] = freq.get(s[end], 0) + 1
            while (end - start + 1) - max(freq.values()) > k:
                freq[s[start]] -= 1
                start += 1
            res = max(res, end - start + 1)
            end += 1
        return res