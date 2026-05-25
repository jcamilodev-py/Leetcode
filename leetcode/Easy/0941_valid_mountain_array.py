class Solution:
    def validMountainArray(self, arr) -> bool:
        if len(arr) >=3:
            if arr[0] < arr[1]:
                for i in range(1, len(arr)):
                    if arr[i] < arr[i+1]:
                        if i+2 < len(arr):
                         continue
                        else:
                            return False
                    else:
                        if arr[i] == arr[i+1]:
                            return False
                        else:
                          for j in range(i, len(arr)-1):
                                if arr[j] > arr[j+1]:
                                   continue
                                else:
                                    return False
                          return True
            else:
                return False
        else:
            return False

s = Solution()
print(s.validMountainArray([0,1,2,3,4,3,2,1]))