class Solution:
    def mostCommonWord(self, paragraph, banned):
        import re
        paragraph = paragraph.lower()
        paragraph = re.sub(r'[^A-Za-zÁÉÍÓÚáéíóúÑñ0-9\s]', ' ', paragraph)
        paragraph = paragraph.split()
        dic = {}
        for i in paragraph:
            if i in banned:
                continue
            else:
                if i in dic:
                    dic[i]+=1
                else:
                    dic[i] = 1
        print(dic, paragraph)
        m = max(dic.values())
        for clave, valor in dic.items():
            if valor == m:
                return clave


s = Solution()
print(s.mostCommonWord("a.", []))