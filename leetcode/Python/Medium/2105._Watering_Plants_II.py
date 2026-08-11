from typing import List


class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        ans = 0
        current1, current2 = capacityA, capacityB
        i, j = 0, n-1

        while i < j:
            if plants[i] <= current1:
                current1-=plants[i]
            else:
                ans+=1
                current1 = capacityA
                current1-=plants[i]

            if plants[j] <= current2:
                current2-=plants[j]
            else:
                ans+=1
                current2 = capacityB
                current2-=plants[j]

            i+=1
            j-=1

        if i == j:
            if current1 > current2:
                if current1 < plants[i]:
                    ans+=1
            elif current1 < current2:
                if current2 < plants[j]:
                    ans+=1
            else:
                if current1 < plants[i]:
                    ans+=1

        return ans
        
        





s = Solution()
print(s.minimumRefill(plants = [2,1,1], capacityA = 2, capacityB = 2))