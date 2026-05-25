class Solution:
    def generateTag(self, caption: str) -> str:
        s = ["#"]
        v = False
        l = 1
        for i in range(len(caption)):
            if caption[i] == " ":
                v = True
                continue
            if v and len(s) > 1:
                s.append(caption[i].capitalize())
                v = False
                l+=1
                continue
            else:
                s.append(caption[i].lower())
                l+=1
                v = False
            if l == 100:
                return "".join(s)
        return "".join(s)



s = Solution()
print(s.generateTag("Leetcode daily streak achieved"))