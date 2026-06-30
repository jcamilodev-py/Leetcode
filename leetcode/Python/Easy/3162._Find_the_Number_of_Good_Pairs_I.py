from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        memo = set()
        ans = 0

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if (nums1[i], nums2[j]) not in memo:
                    if nums1[i] % (nums2[j] * k) == 0:
                        ans+=1
                        memo.add((nums1[i], nums2[j]))
                else:
                    ans+=1
        return ans




s = Solution()
print(s.numberOfPairs([1,3,4], nums2 = [1,3,4], k = 1))