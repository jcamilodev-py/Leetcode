class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0
        indice = 0
        dic = {
            "I":	1,
            "V":	5,
            "X":	10,
            "L":	50,
            "C":	100,
            "D":	500,
            "M":	1000
        }
        while indice != len(s):
               if indice +1< len(s) and dic[s[indice]] < dic[s[indice+1]]:
                  output +=dic[s[indice+1]]- dic[s[indice]]
                  indice+=2
               else:
                output+=dic[s[indice]]
                indice+=1
        return output
    
s = Solution()
print(s.romanToInt("MCMXCIV"))