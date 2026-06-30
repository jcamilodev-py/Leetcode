from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        dic = {}
        alone = 0
        aswner = 0
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i] = 1
        for i in dic.values():
            if i %2 !=0:
                alone+=1
                aswner+= i//2
            else:
                aswner+= i/2
        return [int(aswner), alone]
                
                


s = Solution()
print(s.numberOfPairs([1,1]))



# 👉 Elegir dos números que sean exactamente iguales
# 👉 Quitarlos de la lista al mismo tiempo
# 👉 Esos dos números forman un par

# Y sigues haciendo eso hasta que ya no se pueda más, es decir, hasta que no queden dos números iguales para formar otro par.

# ¿Qué te piden devolver?

# Un arreglo de 2 posiciones:

# answer[0] → Cuántos pares lograste formar en total

# answer[1] → Cuántos números quedaron solos, sin poder formar pareja