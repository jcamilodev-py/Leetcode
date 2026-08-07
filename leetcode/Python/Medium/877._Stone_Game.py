from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        a, b = 0, 0
        n = len(piles)

        i = (n // 2) -1
        j = n // 2
        while i >= 0:
            if piles[i] >= piles[j]:
                a+=piles[i]
                b+=piles[j]
                i-=1
                j+=1
            else:
                a+=piles[j]
                b+=piles[i]
                i-=1
                j+=1

        return True if a > b else False



s = Solution()
print(s.stoneGame([3,7,2,3]))