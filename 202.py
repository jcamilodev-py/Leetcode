class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic = {"b":0, "a":0, "l":0, "o":0, "n":0}

        for i in text:
            if i in dic:
                dic[i]+=1

        if "l" in dic:
            dic["l"] //= 2

        if "o" in dic:
            dic["o"] //= 2 
        

        return min(dic.values())

s = Solution()
print(s.maxNumberOfBalloons("balon"))