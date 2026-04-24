class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp = {}
        for ele in s1:
            mp[ele]=1 + mp.get(ele,0)
        l = 0
        for r in range(len(s2)):
            char_r = s2[r]
            if char_r in mp:
                mp[char_r] -=1
            else:
                while l < r:
                    mp[s2[l]] += 1
                    l += 1
                l = r +1
                continue
            while mp[char_r] < 0 :
                mp[s2[l]] += 1
                l += 1
            if r - l + 1 == len(s1):
                return True
        return False