from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        value  = strs[0]
        j = 0
        for i in range(1, len(strs)):
            while j < len(strs[i]) and j < len(value):
                if value == "":
                    return ""
                if not strs[i][j] == value[j]:
                    break
                else:
                    j+=1

            value = strs[i][:j]
            j=0
            
        return value


s = Solution()
print(s.longestCommonPrefix(["cami","ca","car"]))