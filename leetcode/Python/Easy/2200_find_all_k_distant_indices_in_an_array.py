from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        left = 0
        rigth = 0 
        seen = set()
        for i in range(len(nums)):
            if nums[i] == key:
                left = max(0, i-k)
                rigth = min(len(nums)-1, i+k)
                seen.update(range(left, rigth+1))

        return sorted(list(seen))


s = Solution()
print(s.findKDistantIndices([9,1,2,3,9],9,1))