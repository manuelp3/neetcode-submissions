class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        freq = [[] for i in range(len(nums) + 1)]
        solution = []

        for num in nums:
            map[num] = 1 + map.get(num, 0)

        for value in map:
            freq[map[value]].append(value)

        print(freq)

        start = len(freq) - 1
        while (k > 0):
            while (not freq[start]):
                start-=1
            for num in freq[start]:
                solution.append(num)
                k-=1
            start-=1
        return solution
        