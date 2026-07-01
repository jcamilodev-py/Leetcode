from typing import List

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        i, j, ans, mid = 0, n-1, [], arr[(n - 1) // 2]

        while i <= j:
            a1, a2 = abs(arr[i] - mid), abs(arr[j] - mid)
            if a1 > a2:
                ans.append(arr[i])
                i+=1
            elif a1 < a2:
                ans.append(arr[j])
                j-=1
            else:
                if arr[i] > arr[j]:
                    ans.append(arr[i])
                    i+=1
                else:
                    ans.append(arr[j])
                    j-=1

        
        return ans[:k]


s = Solution()
print(s.getStrongest([513], k = 1))