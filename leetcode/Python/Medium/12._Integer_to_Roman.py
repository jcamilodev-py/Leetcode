class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1 : "I",
        }
        ans = []
        num = str(num)
        r = len(num)-1
        j = 0
        while r != -1:
            need = 10**r
            need*=int(num[j])
            while need != 0:
                for i in dic:
                    while i <= need:
                        ans.append(dic[i])
                        need-=i
            r-=1
            j+=1

        return "".join(ans)
            




s = Solution()
print(s.intToRoman(3749))