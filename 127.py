class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        output = ""
        if str1 + str2 == str2 + str1:
            a = len(str1)
            b = len(str2)

            while b != 0:

                a, b = b, a % b

            return output+str1[:a]
        return output

s = Solution()
print(s.gcdOfStrings("LEET", str2 = "CODE"))