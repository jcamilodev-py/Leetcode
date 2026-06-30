from typing import List

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        seen = set(friends)
        ans = []

        for i in order:
            if i in seen:
                ans.append(i)

        return ans



s = Solution()

print(s.recoverOrder([3,1,2,5,4], friends = [1,3,4]))