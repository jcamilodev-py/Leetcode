class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        dic1,dic2 = {}, {}

        for i in s1:
            if i in dic1:
                dic1[i] = dic1[i] +1
            else:
                dic1[i] = 1
        for j in s2:
            if j in dic2:
                dic2[j] = dic2[j]+1
            else:
                dic2[j] =1
        if dic1 == dic2:
            for i in range(len(s2)):
                for j in range(len(s2)):
                    v1 = s2[i]
                    v2= s2[j]
                    # print(v1,v2)
                    s2 = s2[:i] + v2+ s2[i+1:]

                    s2 = s2[:j] + v1 + s2[j+1:]
                    if s2 == s1:
                        return True
                    else:
                        s2 = s2[:i] + v1 + s2[i+1:]
                        s2 = s2[:j] + v2 + s2[j+1:]
            return False 
        return False

        
s = Solution()
print(s.areAlmostEqual("attack", "defend"))