class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        start, end = 0, 0
        max_length = 0

        while (end < len(s)):
            freq[s[end]] = freq.get(s[end], 0) + 1
            if (end - start + 1 - max(freq.values()) > k):
                freq[s[start]] -= 1
                start += 1
            max_length = max(max_length, end - start + 1)
            end += 1
        return max_length