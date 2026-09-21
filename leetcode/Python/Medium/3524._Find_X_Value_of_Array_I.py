from typing import List


class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dp = [[0] * k for _ in range(n)]

        dp[0][nums[0] % k]+=1
        ans = [0] * k
        ans[nums[0] % k]+=1

        for i in range(1, n):
            dp[i][nums[i] % k] +=1
            ans[nums[i] % k]+=1
            for j in range(k):
                idx = j * nums[i] % k
                dp[i][idx]+= dp[i-1][j]
                ans[idx]+=dp[i-1][j]

        return ans












s = Solution()
print(s.resultArray([1,2,3,4,5], k = 3))