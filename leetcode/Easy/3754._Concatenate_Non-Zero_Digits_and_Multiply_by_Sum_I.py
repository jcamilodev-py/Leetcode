class Solution:
    def sumAndMultiply(self, n: int) -> int:
        ans = []
        x = 0

        for i in str(n):
            if i != "0":
                ans.append(i)
        
        for j in ans:
            x+=int(j)
        
        if not ans:
            return 0
        
        n = int("".join(ans))
        
        return n * x
        



s = Solution()
print(s.sumAndMultiply(0))