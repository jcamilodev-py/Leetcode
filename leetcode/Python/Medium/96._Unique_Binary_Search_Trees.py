class Solution:
    def numTrees(self, n: int) -> int:

        nt = [1] * (n+1)

        for i in range(2, n + 1):
            ans = 0
            for j in range(1, i+1):
                l = j - 1
                r = i - j

                ans+=nt[l] * nt[r]
            nt[i] = ans

        return nt[n]


s = Solution()
print(s.numTrees(3))