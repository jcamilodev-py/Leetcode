class Solution:
    def createTargetArray(self, nums, index):
        target = [None] *len(nums)
        n = 0
        for i in index:
            target.insert(i, nums[n])
            print(i, nums[n])
            n+=1
            target.remove(None)
        return target
        



nums = [1,2,3,4] 
index = [0,0,0,0]
s = Solution()
print(s.createTargetArray(nums, index))


