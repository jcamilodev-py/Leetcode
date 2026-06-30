from typing import List

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        seen1 = set(nums1)
        seen2 = set(nums2)
        seen3 = set(nums3)

        s1 = seen1.intersection(seen2)
        s2 = seen1.intersection(seen3)
        s3 = seen2.intersection(seen3)

        result = s1.union(s2)
        final = result.union(s3)

        return list(final)


s = Solution()
print(s.twoOutOfThree(nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]))