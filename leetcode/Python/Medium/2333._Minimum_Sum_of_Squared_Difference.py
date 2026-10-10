from typing import List


class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)

        diff = []

        for i in range(n):
            diff.append(abs(nums1[i] - nums2[i]))

        m = max(diff)

        b = [0] * (m+1)

        for i in diff:
            b[i]+=1

        k = k1+ k2

        for i in range(m, 0, -1):
            moves = min(b[i], k)
            b[i]-=moves
            b[i-1] +=moves
            k-=moves
            if k == 0: break

        ans = 0

        for i in range(m+1):
            ans+= i**2 * b[i]

        return ans




s = Solution()
print(s.minSumSquareDiff(nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1))