# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    

        temp = ListNode()
        head = temp
        prev_carry = 0
        while l1 or l2:
            
            if l1:
                val1 = l1.val
                l1=l1.next
            else:
                val1 = 0
            if l2:
                val2 = l2.val
                l2=l2.next
            else:
                val2 = 0

            if val1+val2+prev_carry >= 10:
                value = val1+val2-10
                carry = 1
            else:
                value=val1+val2
                carry = 0

            
            temp.next = ListNode(value+prev_carry)
            temp=temp.next
            prev_carry = carry
            if carry:
                temp.next = ListNode(val=carry)
        return head.next
            
                        