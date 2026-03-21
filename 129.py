from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i, j in enumerate(flowerbed):
            left = max(0, i-1)
            right = min(len(flowerbed)-1, i+1)

            if j == 0 and flowerbed[left] == 0 and flowerbed[right] == 0:
                flowerbed[i] = 1
                n-=1
                
        return n <= 0
    

s = Solution()
print(s.canPlaceFlowers([0,0,1,0,0], n = 1))