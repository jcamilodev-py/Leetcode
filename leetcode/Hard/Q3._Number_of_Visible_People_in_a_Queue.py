from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        stack = []
        ans = [0] * n

        for i in range(n-1, -1, -1):
            count = 0
            while stack:
                if stack[-1] > heights[i]:
                    count+=1
                    break
                else:
                    count+=1
                    stack.pop()

            ans[i] = count
            stack.append(heights[i])

        return ans
            



s = Solution()
print(s.canSeePersonsCount([10,6,8,5,11,9]))