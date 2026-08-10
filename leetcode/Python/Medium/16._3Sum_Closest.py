from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        ans = 0
        n = len(nums)
        for i in range(n-2):
            j = i+1
            k = n-1

            while j < k:
                v = nums[i] + nums[j] + nums[k]
                if abs(v - target) < diff:
                    diff = abs(v - target)

                    ans = v
                    print(diff, v, ans)

                if v < target:
                    j+=1

                elif v > target:
                    k-=1
                else:
                    return ans
                
        return ans

            
        


s = Solution()
print(s.threeSumClosest([0,1,2], target = 3))