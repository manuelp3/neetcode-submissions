class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        hashset = set()
        count = 0

        while (end < len(s)):
            while (s[end] in hashset):
                hashset.remove(s[start])
                start+=1
            hashset.add(s[end])
            end+=1
            count = max(count, end - start)
        return count