class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string))
            res += "#"
            res += string
        return res
        
    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        start = 0
        end = start

        while (start < len(s) - 1):
            while (s[end] != "#" and end < len(s) - 1):
                end += 1
            length = s[start:end]
            print(length)
            beginning = end + 1
            last = beginning + int(length)
            string = s[beginning:last]
            res.append(string)
            start = last
            end = start
        return res