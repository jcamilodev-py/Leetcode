class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        dic = {}
        count = 0
        for i in word:
            if i in dic:
                dic[i] = dic[i]+1
            else:
                dic[i] = 1

        for j in dic:
            if chr(abs(ord(j) - 32)) in dic and dic[j] >0:
                count+=1
                dic[j] = 0
                dic[chr(abs(ord(j)-32))] = 0
            elif chr(abs(ord(j) +32)) in dic and dic[j] >0:
                count+=1
                dic[j] = 0
                dic[chr(abs(ord(j)+32))] = 0
        return count

s = Solution()
print(s.numberOfSpecialChars("BBBBBBBBbbbbbbbb"))