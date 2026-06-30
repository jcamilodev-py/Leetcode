class Solution:
    def missingInteger(self, nums) -> int:
        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                continue
            else:
                p = sum(list(range(nums[0], nums[i]+1)))
                while p in nums:
                        p+=1
                return(p)
        if sum(nums) in nums:
             return sum(nums)+1
        return sum(nums)
                    
                
                    


s = Solution()
print(s.missingInteger([38,39]))