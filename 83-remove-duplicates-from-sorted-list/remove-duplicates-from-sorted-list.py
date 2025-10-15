# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(head.val)

        new_head = dummy

        temp = head

        while temp:
            if temp.val != dummy.val:
                dummy.next= ListNode(temp.val)
                dummy = dummy.next

            temp = temp.next

        return new_head
