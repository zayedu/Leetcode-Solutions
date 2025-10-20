# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head  # Connect dummy to the original list
        prev = dummy  # Track the node before current pair
        temp = head

        while temp and temp.next:
            first = temp
            second = temp.next
            
            # Swap the pair
            first.next = second.next
            second.next = first
            prev.next = second
            
            # Move to next pair
            prev = first
            temp = first.next
        
        return dummy.next