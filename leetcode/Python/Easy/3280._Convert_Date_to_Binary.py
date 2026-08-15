class Solution:
    def convertDateToBinary(self, date: str) -> str:
        ans = []

        date = date.split("-")
        for i in date:
            if i [0] == "0":
                ans.append(bin(int(i[1:]))[2:])
            else:
                ans.append(bin(int(i))[2:])

        return "-".join(ans)





s = Solution()
print(s.convertDateToBinary("2080-02-29"))