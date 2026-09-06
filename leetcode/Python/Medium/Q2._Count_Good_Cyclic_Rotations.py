class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:

        n = len(nums)
        
        p = [0] * (n+1)

        for i in range(1, n+1):
            p[i] = nums[i-1] + p[i-1]

        j = 0
        ans = 0
        for i in range(n // 2, n+1):
            
            if p[i] - p[j] > (p[-1] - p[i]) + p[j]:
                ans+=1

            j+=1

        j = 1

        for i in range((n // 2) + 1, n):
            if (p[-1] - p[i]) + p[j] > p[i] - p[j]:
                ans+=1

            j+=1

        return ans

        



s = Solution()
print(s.countGoodRotations([10, 6]))