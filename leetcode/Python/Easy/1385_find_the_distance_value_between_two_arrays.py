from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        i:int = 0
        j:int = 0
        count:int = len(arr1)

        while i <= len(arr1) -1:
          if abs(arr1[i] - arr2[j])<= d:
              count-=1
              i+=1
              j=0
          else:
              j+=1
              if j == len(arr2):
                  i+=1
                  j=0
                  
        return count



s  = Solution()
print(s.findTheDistanceValue(arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2))

# Example 2:

# Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
# Output: 2
# Example 3:

# Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
# Output: 1