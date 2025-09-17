# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = head
        prev_node = None
        while temp:
            
            old_next = temp.next

            temp.next= prev_node

            prev_node = temp
            temp = old_next

        return prev_node