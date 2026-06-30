class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        seen = set({'a', 'e', 'i', 'o', 'u'})
        value = s[:k]
        count = 0
        for i in value:
            if i in seen:
                count+=1
        maximum = count
        for i in range(k, len(s)):

            if s[i-k] in seen:
                count-=1
            if s[i] in seen:
                count+=1
            maximum = max(count, maximum)
        return maximum

s = Solution()
print(s.maxVowels("leetcode", 3))