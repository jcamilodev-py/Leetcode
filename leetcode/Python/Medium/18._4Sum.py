from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        a = -1
        ans = []
        seen = set()
        while a < n - 3:
            a+=1
            b = a+1
            while b < n - 2:
                t = target - (nums[a] + nums[b])
                c = b+1
                d = n-1
                while c < d:
                    if nums[c] + nums[d] > t:
                        d-=1
                    elif nums[c] + nums[d] < t:
                        c+=1   
                    else:
                        if ((nums[a], nums[b], nums[c], nums[d])) not in seen:
                            ans.append([nums[a], nums[b], nums[c], nums[d]])

                        seen.add((nums[a], nums[b], nums[c], nums[d]))

                        while c < d and nums[c] == nums[c+1]: c+=1

                        while c < d and nums[d] == nums[d-1]: d-=1

                        c+=1
                        d-=1                        
                b+=1

        return ans




s = Solution()
print(s.fourSum(nums = [2,2,2,2,2], target = 8))