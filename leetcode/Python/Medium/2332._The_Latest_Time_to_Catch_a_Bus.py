from typing import List

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:

        buses.sort()
        n = len(buses)
        passengers.sort()
        m = len(passengers)
        dic = {}

        for i in buses:
            dic[i] = set()      

        i,j = 0, 0

        while i < n and j < m:
            if passengers[j] <= buses[i] and len(dic[buses[i]]) < capacity:
                    dic[buses[i]].add(passengers[j])
                    j+=1
            else:
                i+=1

        seen = set(passengers)

        if len(dic[buses[-1]]) < capacity:
            candidate = buses[-1]
        else:
            candidate = max(dic[buses[-1]]) -1

        while candidate in seen:
            candidate-=1
        
        return candidate

s = Solution()
print(s.latestTimeCatchTheBus([10,20], passengers = [2,17,18,19], capacity = 2))