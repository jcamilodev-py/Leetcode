from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # n = len(height)
        # max_l = [height[0]] * n
        # max_r = [height[0]] * n
        # min_l_r = [0] * n

        # ans = 0


        # for i in range(1, n):
        #     max_l[i] = max(height[i-1], max_l[i-1])

        
        # for i in range(n-2, -1, -1):
        #     max_r[i] = max(height[i+1], max_r[i+1])
        
        # for i in range(n):
        #     min_l_r[i] = min(max_l[i], max_r[i])

        # for i in range(n):
        #     if min_l_r[i] -  height[i] >0:
        #         ans+=min_l_r[i] - height[i]
        
        # return ans

        n = len(height)
        max_l = height[0]
        max_r = height[-1]
        ans, i, j = 0, 0, n-1

        while i < j:
            if max_l <= max_r:
                i+=1
                max_l = max(height[i], max_l)
                ans+= max_l - height[i]
            else:
                j-=1
                max_r = max(height[j], max_r)
                ans+= max_r - height[j]
        return ans
                        
        
s = Solution()
print(s.trap(height =[4,2,0,3,2,5]))