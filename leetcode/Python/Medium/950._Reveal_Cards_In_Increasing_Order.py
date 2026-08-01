from collections import deque
from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        ans = [0] * n

        d = deque(range(0, n))

        for i in deck:
            j = d.popleft()
            ans[j] = i

            if d:
                d.append(d.popleft())

        return ans

        


    

    
s = Solution()
print(s.deckRevealedIncreasing([1, 2, 3, 4, 5]))