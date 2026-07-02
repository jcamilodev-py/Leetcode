from bisect import bisect_right
from typing import List
from collections import Counter

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        c = Counter(power)
        dic = {}
        powers = []

        for i in c:
            dic[i] = i * c[i]
        
        for i in dic:
            powers.append(i)

        n = len(powers)
        powers.sort()
        
        dp = [0]* (n+1) 

        for i in range(1, n+1):
            j = bisect_right(powers, powers[i-1]-3)
            dp[i] = max(dp[i-1], dic[powers[i-1]] + dp[j])
        
        return dp[n]



s = Solution()
print(s.maximumTotalDamage([7,1,6,6]))