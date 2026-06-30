class Solution:
    def numberOfPoints(self, nums):
        s = set()
        for i in range(len(nums)):
            for j in range(nums[i][0], nums[i][1]+1):
                s.add(j)    
        return (len(s))


            


s = Solution()
print(s.numberOfPoints([[1, 1], [2, 2], [3, 3]]))
        