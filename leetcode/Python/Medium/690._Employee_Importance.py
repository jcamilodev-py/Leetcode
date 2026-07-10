from typing import List

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        dic = {}
        for i in employees:
            dic[i.id] = i
        
        def dfs(id):
            t = dic[id].importance

            for sub in dic[id].subordinates:
                t+=dfs(sub)
            return t
        return dfs(id)
            


employees = [
    Employee(1, 5, [2, 3]),
    Employee(2, 3, []),
    Employee(3, 3, [])
]

s = Solution()
print(s.getImportance(employees, 1))