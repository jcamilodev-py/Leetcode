class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        if ch in word:
          v = word.index(ch)+1
        else:
            return "".join(word)
        
        word = list(word)
        j = v-1
        
        for i in range(v//2):
            word[i], word[j] = word[j], word[i]
            j-=1
        return "".join(word)



s = Solution()
print(s.reversePrefix("abcdefd", ch = "f"))
# Output: "dcbaefd"