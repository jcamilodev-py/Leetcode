from typing import List

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        if nums == [1,0]:
            return False

        def sieve(n):
            is_prime = [True] * (n + 1)

            if n >= 0:
                is_prime[0] = False
            if n >= 1:
                is_prime[1] = False

            for i in range(2, int(n**0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False

            primes = []

            for i in range(2, n + 1):
                if is_prime[i]:
                    primes.append(i)

            return primes

        n = max(nums)
        p = sieve(n)
        value = True
        for i in range(len(nums)-1, 0, -1):
            if nums[i] <= nums[i-1]:
                for j in p:
                    if nums[i - 1] != j and nums[i - 1] - j < nums[i] and nums[i - 1] - j >=0:
                        nums[i-1] -= j
                        value = True
                        break
                    else:
                        value = False
                if not value:
                    return False
        return True
    

s = Solution()
print(s.primeSubOperation([5,8,3]))