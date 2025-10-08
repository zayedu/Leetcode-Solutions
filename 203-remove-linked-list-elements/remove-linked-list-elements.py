# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        new_head = dummy

        temp = head
        while temp:
            
            if temp.val != val:
                dummy.next = ListNode(temp.val)
                dummy = dummy.next

            temp = temp.next

        return new_head.next
