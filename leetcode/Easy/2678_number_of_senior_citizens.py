from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for i in details:
            if int(i[11:13]) > 60:
                ans +=1
        return ans


s = Solution()
print(s.countSeniors(["1313579440F2036","2921522980M5644"]))