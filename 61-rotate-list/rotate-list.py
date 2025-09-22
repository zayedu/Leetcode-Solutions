# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or k == 0:
            return head

        length=1
        tail = head

        while tail.next:
            tail= tail.next
            length +=1

        k = k%length
        if k == 0:
            return head
        temp = head
        for i in range(length-k-1):
            temp = temp.next

        new_head = temp.next
        temp.next = None
        tail.next = head

        return new_head