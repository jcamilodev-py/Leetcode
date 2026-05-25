from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        i,count,j = 0,0,1

        while i < len(nums)-1:
            if i < j and nums[i] + nums[j] < target:
                j+=1
                count+=1
            else:
                j+=1
            if j > len(nums)-1:
                i+=1
                j = i+1
        return count
                
    
  
s = Solution()
print(s.countPairs([-6,2,5,-2,-7,-1,3], -2))