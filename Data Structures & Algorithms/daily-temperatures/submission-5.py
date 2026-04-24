class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        left = 0 
        result = []
        n = len(temperatures)
        while left < len(temperatures):
            for right in range(left+1,n):
                if temperatures[right] > temperatures[left]:
                    result.append(right - left)
                    break
                if right == n-1:
                    result.append(0)
            left +=1
        result.append(0)
        return result
            
