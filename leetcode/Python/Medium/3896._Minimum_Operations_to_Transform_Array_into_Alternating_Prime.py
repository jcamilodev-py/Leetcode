class Solution:
    def minOperations(self, nums: list[int]) -> int:
        def is_prime(number):
            for i in range(2, int(number**0.5)+1):
                if number % i == 0:
                    return False
            return True
        ans = 0
        for i, j in enumerate(nums):
            if i % 2 == 0:
                if j == 1:
                    ans+=1
                else:
                    v = j
                    while not is_prime(v):
                        ans+=1
                        v+=1
            else:
                if j == 2:
                    ans+=2
                else:
                    if j != 1 and is_prime(j):
                        ans+=1
        return ans





s = Solution()
print(s.minOperations([7,8,6,1]))