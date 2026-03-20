class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""

        for x, (i,j) in enumerate(zip(word1, word2)):
            output+=i
            output+=j


        return output + word1[x+1:] if len(word1) > len(word2) else output+word2[x+1:]

        


s = Solution()
print(s.mergeAlternately(word1 = "abc", word2 = "pqr"))