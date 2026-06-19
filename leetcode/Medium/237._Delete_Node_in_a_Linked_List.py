# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        current = node
        while current:
            if current.val == node.val:
                current.val = current.next.val
                current.next = current.next.next
                break
            else:
                current = current.next
        
          

s = Solution()
list1 = ListNode(5)
list1.next = ListNode(1)
list1.next.next = ListNode(9)

print(s.deleteNode(list1))


        