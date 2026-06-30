class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        def recursion(current):
            if current == n:
                return True
            if current > n:
                return False
            

            return recursion(current * 2)
        
        return recursion(1)



s = Solution()
print(s.isPowerOfTwo(16))