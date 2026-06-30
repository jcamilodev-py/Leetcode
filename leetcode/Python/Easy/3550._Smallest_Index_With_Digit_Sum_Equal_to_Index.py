from typing import List

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        current = -1
        summ = 0

        for i, j in enumerate(nums):
            if j > 9:
                current = j
                while current != 0:
                    summ += current % 10
                    current //= 10
                if summ == i:
                    return i
                summ = 0
            else:
                if i == j:
                    return i
        return -1
        


s = Solution()
print(s.smallestIndex([1,10,11]))