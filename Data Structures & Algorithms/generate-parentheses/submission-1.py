class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol = []
        stack = []

        def backtrack(openN, closedN):
            if (openN == closedN == n):
                sol.append("".join(stack))
                return
            if (openN < n):
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if (closedN < openN):
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return sol