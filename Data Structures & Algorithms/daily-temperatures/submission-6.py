class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = []

        for left in range(n):
            found = False
            for right in range(left+1, n):
                if temperatures[right] > temperatures[left]:
                    result.append(right - left)
                    found = True
                    break
            if not found:
                result.append(0)
        return result
            
