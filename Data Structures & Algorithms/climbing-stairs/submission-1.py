class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0] * (n + 1)
        for i in range(n, -1, -1):
            if i == n or i == n - 1:
                arr[i] = 1
                continue
            arr[i] = arr[i + 1] + arr[i + 2]
        return arr[0]