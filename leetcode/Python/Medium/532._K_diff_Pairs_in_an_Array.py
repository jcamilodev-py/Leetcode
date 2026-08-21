from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        seen = set()

        i,j = 0,1

        while j < len(nums):

            if abs(nums[i] - nums[j]) > k:
                i+=1
            elif abs(nums[i] - nums[j]) < k:
                j+=1
            else:
                if (nums[i], nums[j]) not in seen:
                    ans+=1
                    seen.add((nums[i], nums[j]))

                i+=1

            if i == j:
                j+=1

        return ans




s = Solution()
print(s.findPairs([1,2,3,4,5], k = 1))