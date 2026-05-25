class Solution:
    def distinctAverages(self, nums) -> int:
        s = set()
        nums.sort()
        while len(nums) >0:
            x = (nums[0] + nums[-1]) /2
            s.add(x)
            del nums[0]
            del nums[-1]
        return len(s)

s = Solution()
print(s.distinctAverages([1,100]))