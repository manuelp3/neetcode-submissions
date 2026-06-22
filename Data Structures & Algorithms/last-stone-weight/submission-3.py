class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxpq = []
        for num in stones:
            heapq.heappush(maxpq, -num)
        while (len(maxpq) > 1):
            stone1 = -1 * heapq.heappop(maxpq)
            stone2 = -1 * heapq.heappop(maxpq)
            if (stone1 != stone2):
                heapq.heappush(maxpq, -1 * abs(stone1 - stone2))
        if not maxpq:
            return 0
        return abs(maxpq[0])
