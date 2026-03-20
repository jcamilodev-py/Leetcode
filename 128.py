from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_kid = max(candies)
        output = []

        for i in candies:
            if i + extraCandies >= max_kid:
                output.append(True)
            else:
                output.append(False)

        return output

s = Solution()
print(s.kidsWithCandies([4,2,1,1,2], extraCandies = 1))