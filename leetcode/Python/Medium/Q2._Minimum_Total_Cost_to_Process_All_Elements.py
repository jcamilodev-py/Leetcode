class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        MOD = 10** 9 + 7

        ans = 0

        k2 = k
        help = 1

        for i in nums:
            if i < k2:
                k2-=i
            else:
                need = i - k2
                m = (need + k - 1) // k
                cost = (help + help + m - 1) * m // 2
                ans+=cost
                help+=m
                k2+=m * k
                k2-=i

        return ans % MOD



s = Solution()
print(s.minimumCost([1,1,7,14], k = 4))