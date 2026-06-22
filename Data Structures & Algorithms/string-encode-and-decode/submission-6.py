class Solution:

    def encode(self, strs: List[str]) -> str:
        special_character = "#"
        string = ""

        for s in strs:
            string += str(len(s)) + special_character + s
        print(string)
        return string
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i
            while (s[j] != '#'):
                j+=1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            string = str(s[i:j])
            strs.append(string)
            i = j
        return strs