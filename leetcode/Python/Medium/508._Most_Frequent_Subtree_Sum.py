from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(self, root: TreeNode | None) -> list[int]:
        dic = defaultdict(int)

        def postorder(node):
            if node is None:
                return 0

            sl = postorder(node.left)
            sr = postorder(node.right)

            node.val+= sl + sr

            dic[node.val]+=1

            return node.val


        postorder(root)
        m = max(dic.values())
        ans = [i for i in dic if dic[i] == m]

        return ans

        


r = TreeNode(5)
r.left = TreeNode(2)
r.right = TreeNode(-5)

s = Solution()
print(s.findFrequentTreeSum(r))