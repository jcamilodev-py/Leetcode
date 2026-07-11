from typing import List

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i,j = 0,0
        ans = 0

        while j < len(nums2) and i < len(nums1):
            if i <= j:
                if nums1[i] <= nums2[j]:
                    if j - i > ans:
                        ans = j - i
                    
                    j+=1
                else:
                    i+=1
            else:
                j+=1
        return ans

        



s = Solution()
print(s.maxDistance(nums1 = [2,2,2], nums2 = [10,10,1]))