class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        dic = {
            "capitals": 0,
            "not_capital":0
        }

        for i in word:
            if ord(i) >= 65 and ord(i) <=90:
                dic["capitals"]+=1
            else:
                dic["not_capital"]+=1
                
        if dic["capitals"] == 0 or dic["not_capital"] == 0:
            return True
        elif dic["capitals"] == 1 and ord(word[0]) >=65 and ord(word[0]) <=90:
            return True
        return False




s = Solution()
print(s.detectCapitalUse("UUsS"))