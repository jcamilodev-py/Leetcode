from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceSizes.sort()
        bobSizes.sort()
        a = sum(aliceSizes)
        b = sum(bobSizes)
        i,j = 0, 0

        while True:
            if (a - aliceSizes[i]) + bobSizes[j] > (b - bobSizes[j]) + aliceSizes[i]:
                i+=1
            elif (a - aliceSizes[i]) + bobSizes[j] < (b - bobSizes[j]) + aliceSizes[i]:
                j+=1
            else:
                return [aliceSizes[i], bobSizes[j]]




s = Solution()
print(s.fairCandySwap(aliceSizes = [2], bobSizes = [1,3]))