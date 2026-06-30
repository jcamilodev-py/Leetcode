from collections import deque

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        d = deque(range(1,n+1))
        count = 1
        
        while len(d) != 1:
            if count == k:
                count = 1
                d.popleft()
            else:
                d.append(d.popleft())
                count+=1

        return d[0]


        





s = Solution()
print(s.findTheWinner(n = 6, k = 5))