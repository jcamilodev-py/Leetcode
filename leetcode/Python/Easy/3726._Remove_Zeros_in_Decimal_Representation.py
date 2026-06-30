class Solution:
    def removeZeros(self, n: int) -> int:
        ans = 0
        list = [int(d) for d in str(n)]

        for i in list:
            if ans != 0 and i != 0:
                ans = (ans* 10) + i
            elif ans == 0 and i != 0:
                ans+=i
        
        return ans
            



s = Solution()
print(s.removeZeros(1))