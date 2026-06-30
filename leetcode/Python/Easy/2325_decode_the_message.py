class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dic = {}
        dicc = "abcdefghijklmnopqrstuvwxyz"
        output = ""
        key = key.replace(" ", "")
        key = "".join(dict.fromkeys(key))


        for i,j in zip(key, dicc):
              dic[i] = j


        for x in message:
            if x == ' ':
                output += ' '
            else:
                output += dic[x]
        return output



s = Solution()
print(s.decodeMessage("eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb"))