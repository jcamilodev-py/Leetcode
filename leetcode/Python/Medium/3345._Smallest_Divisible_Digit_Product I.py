class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        j = 0
        for _ in range(n, 91):
            ans = 1
            value = n + j
            while value:
                ans*= value % 10
                value//=10

            if ans % t == 0:
                return n + j

            ans = 1
            j+=1


            
s = Solution()
print(s.smallestNumber(15, t = 3))