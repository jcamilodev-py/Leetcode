class Solution:
    def digitCount(self, num: str) -> bool:
        count = 0
        for i in range(len(num)):
            for j in num:
                if i == int(j):
                    count +=1
            if not count == int(num[i]):
                return False
            count = 0
        return True