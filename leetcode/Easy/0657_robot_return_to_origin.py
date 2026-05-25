class Solution:
    def judgeCircle(self, moves: str) -> bool:
        r = 0
        u = 0
        for i in moves:
            if i =="R":
                r+=1
            elif i == "U":
                u+=1
            elif  i == "L":
                r-=1
            else:
                u-=1
        return r ==0 and u == 0



s = Solution()
print(s.judgeCircle("RRDD"))