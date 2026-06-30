from collections import Counter

class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        ans = 0
        count = Counter(str(n))
        for i in count:
            ans+=(int(i) * count[i])
        
        return ans



s = Solution()
print(s.digitFrequencyScore(101))