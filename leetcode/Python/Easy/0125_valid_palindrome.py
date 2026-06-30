class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0

        end = len(s)
        s=s.lower()
        while start < end:
            if s[start].isalnum():
                if s[end-1].isalnum():
                    if s[start] == s[end-1]:
                     start+=1
                     end-=1
                    else:
                      return False
                else:
                    end-=1
            else:
                start+=1
        return True
    
s = Solution()
print(s.isPalindrome("race a car"))


print(len(".,"))
