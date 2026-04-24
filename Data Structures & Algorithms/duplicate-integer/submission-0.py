class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_ = {}
        for num in nums:
            dict_[num] = dict_.get(num,0)+1

        for key,value in dict_.items():
            if value > 1:
                return True
        return False