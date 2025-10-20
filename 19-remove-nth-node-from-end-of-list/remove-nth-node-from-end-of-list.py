# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def length(head):
            if not head:
                return 0

            length = 0

            while head:
                length += 1
                head=head.next

            return length

        temp = head

        length = length(temp)
        idx = length -n 

        temp =head
        count = 0 
        if length - n == 0:
            return head.next
        while temp:
            if count == idx-1:
                temp.next = temp.next.next
            count += 1
            temp = temp.next

        return head
