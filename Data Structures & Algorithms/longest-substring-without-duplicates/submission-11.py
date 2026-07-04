class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 1
        if (len(s) < 1):
            return 0
        else:
            chars = set(s[start])
            max_len = 1

        while (end < len(s)):
            if (s[end] in chars):
                while (s[end] in chars):
                    chars.remove(s[start])
                    start += 1
            else:
                max_len = max(max_len, end - start + 1)
            chars.add(s[end])
            end += 1
        return max_len