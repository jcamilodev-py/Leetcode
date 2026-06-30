class Solution:
    def maximum69Number (self, num: int) -> int:
        n = str(num)
        for i in range(len(n)):
            if n[i] == "6":
                return int(n[:i] + "9" + n[i+1:])
        return num


s = Solution()
print(s.maximum69Number(9999))