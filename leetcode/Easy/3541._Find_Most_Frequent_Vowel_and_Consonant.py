class Solution:
    def maxFreqSum(self, s: str) -> int:
        dic = {}
        vowel = set("aeiou")
        consonant = set("bcdfghjklmnpqrstvwxyz")
        max_vowel = 0
        max_consonant = 0

        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i]+=1
        
        for i in dic:
            if i in vowel and dic[i] > max_vowel:
                max_vowel = dic[i]
            elif i in consonant and dic[i] > max_consonant:
                max_consonant = dic[i]
        
        return max_vowel + max_consonant
        



s = Solution()
print(s.maxFreqSum("successes"))