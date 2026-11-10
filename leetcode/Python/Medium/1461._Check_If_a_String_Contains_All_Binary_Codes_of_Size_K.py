class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        used = set()

        for i in range(len(s)-(k-1)):
            used.add(s[i:k+i])


        return True if len(used) == 2 ** k else False



s = Solution()
print(s.hasAllCodes("00110", 2))