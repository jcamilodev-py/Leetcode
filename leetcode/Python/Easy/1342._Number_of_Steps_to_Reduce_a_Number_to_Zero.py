class Solution:
    def numberOfSteps(self, num: int) -> int:

        n = str(bin(num))

        return (len(n[2:]) - 1) + n.count("1")

s = Solution()
print(s.numberOfSteps(123))