class Solution:
    def calPoints(self, operations):
        record = []
        for i in operations:
            if i == "C":
                record.pop()
            else:
                if i == "D":
                    record.append(int(record[-1])*2)
                else:
                  if i == "+":
                      suma = int(record[-1]) + int(record[-2])
                      record.append(suma)
                  else:
                     record.append(int(i))
        return sum(record)




s = Solution()
print(s.calPoints(["1","C"]))
# Input: ops = ["5","2","C","D","+"]
# Output: 30
# "x" (número)	Agrega x al registro
# "C"	Borra el último puntaje
# "D"	Agrega el doble del último puntaje
# "+"	Agrega la suma de los dos últimos puntajes