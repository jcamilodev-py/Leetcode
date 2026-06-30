class Solution:
    def maxOperations(self, nums) -> int:
        if len(nums) >1:
            output = 1
        else:
         output=0
        for i in range(2, len(nums), 2):
            b = nums[0] + nums[1]
            if len(nums) > i+1 and nums[i] + nums[i+1] == b:
                output+=1
            else:
                break
        return output
            


s = Solution()
print(s.maxOperations([2,2,3,2,4,2,3,3,1,3]))