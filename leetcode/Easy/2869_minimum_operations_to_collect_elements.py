class Solution:
    def minOperations(self, nums, k: int) -> int:
        seen = set(range(1,k+1))
        count = 0
        for i in reversed(nums):
            if len(seen)>0:
                if i in seen:
                 seen.remove(i)
                 count+=1
                else:
                  count+=1
            else:
             return count
        return count



s = Solution()
print(s.minOperations([1,2,3,4,5], 3))