# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = ListNode()
        head = temp
        carry = 0

        while l1 or l2:

            if l1:
                val1 = l1.val
                l1=l1.next
            else:
                val1 = 0

            if l2:
                val2=l2.val
                l2=l2.next
            else:
                val2=0

            carry_sum = carry+val1+val2

            if carry_sum >= 10:
                carry_sum -= 10
                carry = 1
            else:
                carry = 0

            temp.next = ListNode(carry_sum)
            temp = temp.next
        

        if carry:
            temp.next = ListNode(carry)

        return head.next