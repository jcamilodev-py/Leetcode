class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        s1 = bin(a)
        s2 = bin(b)

        a, b = 0, 0

        for i in s1[2:]:
            if i == "1":
                a+=1

        for i in s2[2:]:
            if i == "1":
                b+=1

        return a * b if a >= b else b // a






s = Solution()
print(s.calculateScore(14, b = 6))