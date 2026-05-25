from typing import List, Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        seen = set()
        
        for i in count.values():
            if i in seen:
                return False
            seen.add(i)
        return True



s = Solution()
print(s.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))