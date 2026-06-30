from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums 
        nn = len(nums)
        ans = []
        count = 1


        for i in range(1, nn):
            if nums[i]-1 == nums[i-1]:
                count+=1 
            else:
                count = 1

            if i >= k-1:
                if count >= k:
                    ans.append(nums[i])
                else:
                    ans.append(-1)

        
        return ans


s = Solution()
print(s.resultsArray([4,3,1,2,3,4,5,5,6,5], 4))