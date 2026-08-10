class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n-2):
            j = i+1
            k = n-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            while j < k:
                if nums[j] + nums[k] > target:
                    k-=1
                elif nums[j] + nums[k] < target:
                    j+=1
                else:
                    ans.append([nums[i], nums[j], nums[k]])

                    while j < k and nums[j] == nums[j+1]: j+=1

                    while j < k and nums[k] == nums[k-1]: k-=1

                    j+=1
                    k-=1

                    
        return ans               



s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))