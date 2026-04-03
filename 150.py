from typing import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ans = 0
        dic = {
            "type": 0,
            "color": 1,
            "name": 2
        }
        for i in items:
            if i[dic[ruleKey]] == ruleValue:
                ans+=1
        return ans


s = Solution()
print(s.countMatches(items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"))