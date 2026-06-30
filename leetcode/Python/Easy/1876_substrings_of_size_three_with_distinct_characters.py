class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n=3
        count = 0
        for i in range(len(s)):
            value = s[i:n]
            if len(value) <3:
                break
            if value[0] != value[1] and value[1] != value[2] and value[0] != value[2]:
                count +=1
                n+=1
            n+=1
        return count







s = Solution()
print(s.countGoodSubstrings("aababcabc"))


# Example 1:

# Input: s = "xyzzaz"
# Output: 1
# Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
# The only good substring of length 3 is "xyz".
# Example 2:

# Input: s = "aababcabc"
# Output: 4
# Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
# The good substrings are "abc", "bca", "cab", and "abc".