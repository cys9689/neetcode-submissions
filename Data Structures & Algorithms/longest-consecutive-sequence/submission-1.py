class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(list(set(nums)))
        result = 1
        temp = 1
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                temp += 1
                result = max(result,temp)
            else:
                temp =1
        return result