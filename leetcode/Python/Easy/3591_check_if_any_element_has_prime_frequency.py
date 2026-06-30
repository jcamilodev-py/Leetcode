from typing import List
import math

# from collections import defaultdict
# d = defaultdict(int)
# for i in nums:
#     d[i] += 1
class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        for j in dic.values():
            if j > 1: 
                es_primo = True
                for x in range(2, int(math.sqrt(j)) + 1):
                    if j % x == 0:
                        es_primo = False
                        break
                
                if es_primo:
                    return True   

        return False  
    
s = Solution()
print(s.checkPrimeFrequency([2,2,2,4,4]))