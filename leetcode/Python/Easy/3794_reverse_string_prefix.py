class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        lista = []
        lista.append(s[k-1::-1])
        lista.append(s[k:])
        return "".join(lista)
    
        # lista = []
        # pointer1 = k-1
        # while True:    
        #     lista.append(s[pointer1])
        #     pointer1-=1
        #     if pointer1 < 0:
        #         lista.append(s[k:])
        #         break
        # return "".join(lista)




s = Solution()
print(s.reversePrefix("x", 1))





# Input: s = "abcd", k = 2

# Output: "bacd"

# Explanation:​​​​​​​

# The first k = 2 characters "ab" are reversed to "ba". The final resulting string is "bacd".