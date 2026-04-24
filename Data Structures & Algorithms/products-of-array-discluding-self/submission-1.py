import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # return the product of the element except itself
        # method 1 : 一個for loop append 所有的element except itself
        # example [[2,4,6],[1,4,6],[1,2,6],[1,2,4]] 
        # conclusion -> O(n^2)
        # method 2 : 一個for loop 儲存 product[nums] / nums[i]
        # example : [48/1,48/2,48/4,48/6]
        # conoclusion -> method 2 needs to handle zero condition
        # method 3 : prefix and suffix technique
        # [1,2,4,6] -> prefix = [1,0,0,0] -> pref[1] = pref[0] * nums[0]
        # example prefix = [1,2,6,24] suffix = [24,24,12,4] -> output : [24,12,8,6]
        n = len(nums)
        res = [1] * n
        prefix = 1 
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(n-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

 
