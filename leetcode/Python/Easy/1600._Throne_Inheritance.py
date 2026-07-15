from typing import List

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.dic = {kingName: []}
        self.deathh = set()

    def birth(self, parentName: str, childName: str) -> None:
        if parentName in self.dic:
            self.dic[parentName].append(childName)
        else:
            self.dic[parentName] = [childName]

    def death(self, name: str) -> None:
        self.deathh.add(name)
        

    def getInheritanceOrder(self) -> List[str]:
        ans = [self.king] if self.king not in self.deathh else []
        def dfs(fromm, ans):
            
            if not fromm in self.dic or not self.dic[fromm]:
                return ans

            for i in self.dic[fromm]:
                if i not in self.deathh:
                    ans.append(i)

                dfs(i, ans)
            return ans
                    
            
        return dfs(self.king, ans)



# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

o = ThroneInheritance("king")
o.birth("king", "andy")
o.birth("king", "bob")
o.birth("king", "catherine")
o.birth("andy", "matthew")
o.birth("bob", "alex")
o.birth("bob", "asha")
print(o.getInheritanceOrder())
o.death("bob")
print(o.getInheritanceOrder())