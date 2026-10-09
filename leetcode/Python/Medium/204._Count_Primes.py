class Solution:
    def countPrimes(self, n: int) -> int:

        def criba(value):
            if value == 0 or value == 1:
                return 0
            is_prime = [True] * (value+1)
            is_prime[0] = is_prime[1] = False

            for i in range(2, int(value ** 0.5) + 1):
                if is_prime[i]:
                    is_prime[i*i::i] = [False] * len(range(i*i, value+1, i))

            return len([i for i in range(2, value+1) if is_prime[i] and i < n])

        return criba(n)





s = Solution()
print(s.countPrimes(2))