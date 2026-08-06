from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def r(pre, post):
            if len(pre) == 0:
                return 
            if len(pre) == 1:
                root = TreeNode(pre[0])
                return root
            root = TreeNode(pre[0])

            for i in range(len(post)):
                if post[i] == pre[1]:
                    l = i+1
                    pre_l = pre[1: l+1]
                    pre_r = pre[l+1:]
                    post_l = post[:l]
                    post_r = post[l: -1]

            root.left = r(pre_l, post_l)
            root.right = r(pre_r, post_r)

            return root

        return r(preorder, postorder)

                




s = Solution()
print(s.constructFromPrePost(preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]))