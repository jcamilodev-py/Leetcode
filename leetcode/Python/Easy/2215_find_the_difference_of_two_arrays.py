from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        seen = set(nums1)
        seen2 = set(nums2)
        answer = [list(seen - seen2), list(seen2 - seen)]
        return answer

        


s = Solution()
print(s.findDifference([1,2,3,3], nums2 = [1,1,2,2]))