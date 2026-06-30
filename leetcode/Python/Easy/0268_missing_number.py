class Solution:
    def missingNumber(self, nums) -> int:
        seen = set(range(0, len(nums)+1))
        nums.sort()
        for i,j in zip(nums, seen):
            print(i,j)
            if i != j:
                return j
        return j+1
    
        # for i in nums:
        #     if i in seen:
        #         seen.remove(i)
        # return seen



s = Solution()
print(s.missingNumber([0,1]))