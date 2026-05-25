class Solution:
    def reverseByType(self, s: str) -> str:
        l, sim, output = "", "", ""
        i1,i2 = len(l)-1, len(sim)-1
        for i in s:
            if i.islower():
                l+=i
            else:
                sim+=i

        for j in s:
            if j.islower():
                output+=l[i1]
                i1-=1
            else:
                output +=sim[i2]
                i2-=1
        return output
    
    
s = Solution()
print(s.reverseByType("!@#$%^&*()"))