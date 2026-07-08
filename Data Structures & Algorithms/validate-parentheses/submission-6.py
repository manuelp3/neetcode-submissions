class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if (char == '(' or char == '{' or char == '['):
                stack.append(char)
            else:
                if not stack:
                    return False
                closed = stack.pop()
                if (closed == '('):
                    if char != ')':
                        return False
                elif (closed == '{'):
                    if char != '}':
                        return False
                else:
                    if char != ']':
                        return False
        return not stack