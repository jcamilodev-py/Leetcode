class Solution:
    def oddString(self, words):
        dic = {
            'a':0,
            'b':1,
            'c':2,
            'd':3,
            'e':4,
            'f':5,
            'g':6,
            'h':7,
            'i':8,
            'j':9,
            'k':10,
            'l':11,
            'm':12,
            'n':13,
            'o':14,
            'p':15,
            'q':16,
            'r':17,
            's':18,
            't':19,
            'u':20,
            'v':21,
            'w':22,
            'x':23,
            'y':24,
            'z':25
        }
        lista = []
        dic_c = {}
        for i in range(len(words)):
            for j in range(len(words[0])-1):

                lista.append(dic[words[i][j+1]] - dic[words[i][j]])
            if tuple(lista) not in dic_c:
                dic_c[tuple(lista)] =[words[i]]
                lista.clear()
            else:
                dic_c[tuple(lista)].append(words[i])
                lista.clear()
            
        for i in dic_c:
            if len(dic_c[i]) == 1:
                return "".join(dic_c[i])
            
            
        


s = Solution()
print(s.oddString(["adc","wzy","abc"]))