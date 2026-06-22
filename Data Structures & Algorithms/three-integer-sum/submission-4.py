class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        nums.sort()

        for index, num in enumerate(nums):
            if (index > 0 and num == nums[index-1]):
                continue
            
            target = -num
            start, end = index + 1, len(nums) - 1

            while (start < end):
                if (nums[start] + nums[end] < target):
                    start+=1
                elif (nums[start] + nums[end] > target):
                    end-=1
                else:
                    arr.append([num, nums[start], nums[end]])
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    start+=1
        return arr
            
