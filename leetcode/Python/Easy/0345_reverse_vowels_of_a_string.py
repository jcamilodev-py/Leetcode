class Solution:
    def reverseVowels(self, s: str) -> str:
        seen = set('aeiouAEIOU')
        vocals = []
        for i in s:
            if i in seen:
                vocals.append(i)
                
        x = len(vocals)-1

        for j,l in enumerate(s):

            if l in seen:
                s = s[:j] + vocals[x] +s[j+1:]
                x-=1

        return s


s = Solution()
print(s.reverseVowels("leetcode"))
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".