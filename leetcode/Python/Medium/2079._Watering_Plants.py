from typing import List

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        n = len(plants)

        ans = 0
        current = capacity

        for i in range(n):
            ans+=1

            if current >= plants[i]:
                current-=plants[i]
            else:
                current = capacity
                ans+=i+i
                current-=plants[i]

        return ans




s = Solution()
print(s.wateringPlants([2,2,3,3], capacity = 5))