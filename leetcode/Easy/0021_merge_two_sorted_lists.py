from typing import Optional
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = list1
        current2 = list2

        new_node = ListNode(0)
        current_new_node = new_node

        while current1 != None and current2 != None:
            if current1.val <= current2.val:
                current_new_node.next = ListNode(current1.val)
                current1 = current1.next
            else:
                current_new_node.next = ListNode(current2.val)
                current2 = current2.next

            current_new_node = current_new_node.next

        while current1 != None:
            current_new_node.next = ListNode(current1.val)
            current_new_node = current_new_node.next
            current1 = current1.next

        while current2 != None:
            current_new_node.next = ListNode(current2.val)
            current_new_node = current_new_node.next
            current2 = current2.next


        return new_node.next
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
            




s = Solution()
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

print(s.mergeTwoLists(list1, list2))

# Output: [1,1,2,3,4,4]
