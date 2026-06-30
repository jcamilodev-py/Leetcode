from typing import List, Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = Counter(digits)
        res = []
        for num in range(100, 1000, 2):
            a = num // 100
            b = num % 100 // 10
            c = num % 10
            freq[a]-=1
            freq[b]-=1
            freq[c]-=1
            if freq[a] >= 0 and freq[b] >= 0 and freq[c] >= 0:
                res.append(num)
            freq[a] +=1
            freq[b] +=1
            freq[c] +=1

        return res



s = Solution()
print(s.findEvenNumbers([2,1,3,0]))