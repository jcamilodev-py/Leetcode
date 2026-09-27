from collections import defaultdict

class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        dic = defaultdict(int)

        equal = 0

        for i in range(len(nums)-1):

            a,b = nums[i], nums[i+1]

            if a == b:
                equal+=1
            else:
                k = (a,b) if a < b else (b,a)
                dic[k]+=1

        ans = max(dic.values(), default=0)

        return ans + equal


s = Solution()
print(s.maxEqualAdjacentPairs([1,2,3,2]))