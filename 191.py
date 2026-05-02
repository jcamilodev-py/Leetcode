class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans  = list(address)
        for i,j in enumerate(ans):
            if j == ".":
                ans[i] = "[.]"
        return "".join(ans)



s = Solution()
print(s.defangIPaddr("255.100.50.0"))