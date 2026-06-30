from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        n = len(gas)
        ans, current = 0, 0
        for i in range(n):
            current+=gas[i] - cost[i]
            if current < 0:
                ans = i + 1
                current = 0
        
        return ans


s = Solution()
print(s.canCompleteCircuit(gas = [5,1,2,3,4], cost = [4,4,1,5,1]))