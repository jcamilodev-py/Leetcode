from typing import List
from math import gcd

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        dic  = {}

        for i in deck:
            if i in dic:
                dic[i] +=1
            else: 
                dic[i] = 1
        
        l = list(dic.values())
        x = l[0]
        for j in dic.values():
            x = gcd(x, j)
        
        return True if x > 1 else False
  
        
    
s = Solution()
print(s.hasGroupsSizeX([1,1,1,1,1,0,0,0]))