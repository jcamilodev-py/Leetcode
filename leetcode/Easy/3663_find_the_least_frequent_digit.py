class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        dic = {}
        for i in str(n):
            if i in dic:
                dic[i] = dic[i]+1
            else:
                dic[i] = 1
        lista = []        
        for j in dic:
            if dic[j] == min(dic.values()):
                lista.append(j)
        
        return(int(min(lista)))
    



s = Solution()
print(s.getLeastFrequentDigit(723344511))