from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        p = [0] * (n+1)
        avg = [-1] * n
        value = k*2+1

        for i in range(1, n+1):
            p[i] = p[i-1] + nums[i-1]
        i,j = 0, value

        while j < n+1:
            avg[k] = (p[j] - p[i]) // value
            i+=1
            j+=1
            k+=1
        
        return avg



s = Solution()
print(s.getAverages(nums = [8], k = 100000))