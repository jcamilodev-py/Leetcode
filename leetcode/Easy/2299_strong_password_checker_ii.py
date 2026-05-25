class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        seen = set({"!","@","#","$","%","^","&","*","(",")","-","+"})
        numbers = set({"1","2","3","4","5","6","7","8","9","0"})
        password +="x"
        lower = 0
        capitalize = 0
        digits = 0
        symbols = 0

        n = len(password)
        for i in range(n-1):
            if password[i] == password[i+1]:
                return False

            if password[i] in seen:
                symbols+=1

            elif password[i] in numbers:
                digits+=1

            elif password[i] == password[i].lower():
                lower+=1
            else:
                capitalize +=1

        if n-1 >= 8 and lower >=1 and capitalize >=1 and digits >=1 and symbols >=1:
            return True
        return False


s = Solution()
print(s.strongPasswordCheckerII("Me+You--IsMyDream"))