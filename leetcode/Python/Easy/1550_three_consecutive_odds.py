from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        ans = 0
        for i in arr:
            if i % 2 !=0:
                ans +=1
                if ans == 3:
                    return True
            else:
                ans = 0
        return False
    
s = Solution()
print(s.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))
            
                