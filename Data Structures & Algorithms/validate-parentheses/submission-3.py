class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesis = {')' : '(', '}' : '{', ']' : '['}

        for char in s:
            if (char in parenthesis):
                if not stack or stack.pop() != parenthesis[char]:
                    return False
            else:
                stack.append(char)
        
        return not stack