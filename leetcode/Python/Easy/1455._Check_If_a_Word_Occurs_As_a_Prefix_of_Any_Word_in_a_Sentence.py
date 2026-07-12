class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:

        sentence = sentence.split()
        n = len(sentence)
        m = len(searchWord)

        for i in range(n):
            if sentence[i][0] == searchWord[0] and sentence[i][:m] == searchWord:
                return i+1
        return -1

s = Solution()
print(s.isPrefixOfWord(sentence = "i am tired", searchWord = "you"))