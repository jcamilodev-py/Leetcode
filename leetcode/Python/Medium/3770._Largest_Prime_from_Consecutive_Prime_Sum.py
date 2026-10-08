
class Solution:
    def largestPrime(self, n: int) -> int:
        def criba(n):
            is_prime = [True] * (n+1)
            is_prime[0] = is_prime[1] = False

            for i in range(2, int(n**0.5)+1):
                if is_prime[i]:
                    is_prime[i*i::i] = [False] * len(range(i*i, n+1, i))

            current, ans = 0, 0

            for i in range(2, n+1):
                if is_prime[i]:
                    if current+i > n:
                        break
                    current+=i
                    if is_prime[current]:
                        ans = max(ans, current)

                if current > n:
                    break

            return ans

        return criba(n)





s = Solution()
print(s.largestPrime(2))