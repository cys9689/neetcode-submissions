class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dict_ = {}
        for num in nums:
            if num in dict_:
                return num
            else:
                dict_[num] = 1
