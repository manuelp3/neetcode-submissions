class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string))
            res += "#"
            res += string
        return res
        
    def decode(self, s: str) -> List[str]:
        res = []
        start = end = 0

        while (start < len(s) - 1):
            while (s[end] != "#"):
                end += 1
            length = s[start:end]
            first = end + 1
            last = first + int(length)
            string = s[first:last]
            res.append(string)
            start = end = last
        return res