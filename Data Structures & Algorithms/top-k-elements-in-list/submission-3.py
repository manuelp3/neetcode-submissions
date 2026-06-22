class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        yo = sorted(freq.items(), key=lambda x: x[1])

        res = []
        for i in range(len(yo) - 1, len(yo) - k - 1, -1):
            res.append(yo[i][0])
        return res