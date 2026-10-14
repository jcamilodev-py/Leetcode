class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:

        def criba(value):
            is_prime = [True] * (value+1)
            is_prime[0] = is_prime[1] = False

            for i in range(2, int(value ** 0.5)+1):
                if is_prime[i]:
                    is_prime[i*i::i] = [False] * len(range(i*i, value+1, i))

            return [i for i in range(2, value+1) if is_prime[i]]


        c = criba(n)
        ans = []
        current_sum = 0

        for i in c:
            if current_sum + i <= s:
                current_sum+=i
                ans.append(i)
            else:
                return ans
        return ans





s = Solution()
print(s.maxPrimes(n = 3, s = 2))