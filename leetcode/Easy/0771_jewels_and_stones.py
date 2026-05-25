class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        from typing import Counter
        count = 0
        d = Counter(stones)
        for i in jewels:
            if i in d:
                count+=d[i]
        return count

s = Solution()
print(s.numJewelsInStones("z", "zasasaazz"))