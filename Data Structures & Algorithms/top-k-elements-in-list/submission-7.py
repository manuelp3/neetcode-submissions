class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = [[] for i in range(len(nums) + 1)]

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for number, frequency in freq.items():
            bucket[frequency].append(number)
        
        res = []

        for i in range(len(bucket) - 1, -1, -1):
            for item in bucket[i]:
                res.append(item)
                if len(res) == k:
                    return res