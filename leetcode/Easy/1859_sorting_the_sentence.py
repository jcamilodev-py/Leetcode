class Solution:
    def sortSentence(self, s: str) -> str:
        word = s.split(" ")
        ans = [0] * len(word)

        for i in word:
            ans[int(i[-1])-1] = i[:-1]
        return " ".join(ans)
            






s = Solution()
print(s.sortSentence("Myself2 Me1 I4 and3"))