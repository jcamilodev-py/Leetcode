from typing import List, Counter

class Solution:
    def compress(self, chars: List[str]) -> int:
        count = Counter(chars)
        s = ""
        for i,j in count.items():
            if j == 1:
                s+=i
            else:
                s+=i
                s+=str(j)
        return len(s)


s = Solution()
print(s.compress(["a","a","b","b","c","c","c"]))