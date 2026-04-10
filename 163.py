from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i,j = 0, n-1

        current_max = 0

        while i < j:
            minimum = min(height[i], height[j])
            value = abs(i-j) * minimum

            if value > current_max:
                current_max = value
            
            if height[i] < height[j]:
                i+=1
            elif height[i] > height[j]:
                j-=1
            else:
                if height[i+1] > height[j-1]:
                    i+=1
                else:
                    j-=1
        return current_max
            



s = Solution()
print(s.maxArea([0,2]))