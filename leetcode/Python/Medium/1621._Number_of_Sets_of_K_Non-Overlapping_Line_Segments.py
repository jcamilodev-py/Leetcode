class Solution:
    def numberOfSets(self, n: int, k: int) -> int:

        mod = 10 ** 9 + 7
        max_n = 2001

        m = ((n-1-k) + (2*k+1) -1)
        g = 2 * k

        fact = [1] * max_n

        for i in range(1, max_n):
            fact[i] = fact[i-1] * i % mod

        ans = fact[m] * pow(fact[g], mod-2, mod) % mod * pow(fact[m-g], mod-2, mod) % mod

        return ans



        
        

s = Solution()
print(s.numberOfSets(n = 4, k = 2))