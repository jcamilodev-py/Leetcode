from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i,j = 0,0
        while i <= len(nums1)-1 and j <= len(nums2)-1:
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                j+=1
        return -1

s = Solution()
print(s.getCommon([1,2,4], [3]))
# output :2
        