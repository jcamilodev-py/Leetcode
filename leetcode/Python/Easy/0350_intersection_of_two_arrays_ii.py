from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i,j = 0,0
        nums1.sort()
        nums2.sort()
        output = []
        
        while i < len(nums1) and j < len(nums2):

            if nums1[i] < nums2[j]:
                i+=1

            elif nums1[i] == nums2[j]:
                output.append(nums1[i])
                i+=1
                j+=1

            else:
                j+=1

        return output 


# [1,2,2,1], nums2 = [2,2]
s = Solution()
print(s.intersect([1,2,2,1], nums2 = [2,2]))