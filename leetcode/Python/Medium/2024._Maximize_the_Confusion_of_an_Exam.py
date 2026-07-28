class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        maximum, i = 0, 0

        dic = {"T": 0, "F": 0}
        n = len(answerKey)
        for j in range(n):
            dic[answerKey[j]]+=1

            maximum = max(maximum, dic[answerKey[j]])

            if j - i + 1 > maximum + k:
                dic[answerKey[i]]-=1
                i+=1

        return n - i




s = Solution()
print(s.maxConsecutiveAnswers("FFFTTFTTFT", 3))