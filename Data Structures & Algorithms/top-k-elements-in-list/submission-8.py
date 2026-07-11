class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        heap = []

        for num in freq:
            heapq.heappush(heap, (-freq[num], num))
        
        res = []
        
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        return res