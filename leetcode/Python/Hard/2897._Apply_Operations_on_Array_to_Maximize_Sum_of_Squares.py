from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        b = [0] * 30 # 10 ** 9
        ans = 0
        for i in nums:
            for j in range(30):
                b[j] += (i >> j) & 1

        for _ in range(k):
            current = 0
            for i in range(30):
                if b[i]:
                    current |= 1 << i
                    b[i]-=1

            ans = (ans + current ** 2) % (10 ** 9 + 7)

        return ans

            

s = Solution()
print(s.maxSum([2,6,5,8], k = 2))