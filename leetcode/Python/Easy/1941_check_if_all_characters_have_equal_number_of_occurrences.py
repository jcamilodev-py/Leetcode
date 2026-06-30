# from typing import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dic = {}
        for i in s:
            if i in dic:
                dic[i] = dic[i]+1
            else:
                dic[i] = 1
        l = list(dic.values())
        for i in range(len(l)-1):
            if l[i] != l[i+1]:
                return False
        return True
        # d = Counter(s)
        # print(d)
        # o = None
        # for k in d:
        #     if o is None:
        #         o = d[k]
        #     elif d[k] != o:
        #         return False
        # return True

    
       
            


s = Solution()
print(s.areOccurrencesEqual("aA"))