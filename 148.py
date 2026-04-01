class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        v = 1
        s = 0
        for i in list(str(n)):
            v = v * int(i)
            s+=int(i)
        return v - s
        

s = Solution()
print(s.subtractProductAndSum(4421))

