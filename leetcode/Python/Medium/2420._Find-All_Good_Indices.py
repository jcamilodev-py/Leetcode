class Solution:
    def goodIndices(self, nums: list[int], k: int) -> list[int]:
        ans = []

        n = len(nums)

        dec = [1] * n
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                dec[i] = dec[i - 1] + 1

        inc = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                inc[i] = inc[i + 1] + 1

        for i in range(k, n - k):
            if dec[i-1] >= k and inc[i+1] >= k:
                ans.append(i)

        return ans

    


s = Solution()
print(s.goodIndices([2,1,1,1,3,4,1], k = 2))