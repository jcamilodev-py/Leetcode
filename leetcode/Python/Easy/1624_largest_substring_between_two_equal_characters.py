class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        count = -1

        for i,j in enumerate(s):
            if s[i:].count(j) >= 2:
                for l in range(len(s) - 1, -1, -1):
                    if s[l] == j:

                        if (l - i)  > count:

                            count= (l - i) -1

        return count

    # class Solution:
    # def maxLengthBetweenEqualCharacters(self, s: str) -> int:
    #     mp={}
    #     ans=-1
    #     for i,c in enumerate(s):
    #         if c in mp:
    #             ans=max(ans,i-mp[c]-1)
    #         else:
    #             mp[c]=i
    #     return ans
        
      
s = Solution()
print(s.maxLengthBetweenEqualCharacters("abcaada"))