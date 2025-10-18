# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        new_head = dummy

        while head:

            if head.val != val:
                dummy.next = ListNode(head.val)
                dummy= dummy.next

            head = head.next

        return new_head.next