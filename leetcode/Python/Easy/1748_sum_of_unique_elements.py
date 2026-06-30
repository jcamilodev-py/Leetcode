class Solution:
    def sumOfUnique(self, nums) -> int:
        from typing import Counter
        d = Counter(nums)
        count = 0
        for i in d:
            if d[i] ==1:
                count+=i
        return count



s = Solution()
print(s.sumOfUnique([1,2,3,4,5]))