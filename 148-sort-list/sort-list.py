# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getMid(self,head):
        
        slow = fast = head
        fast = fast.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self,l1,l2):
        dummy = ListNode()
        new_head = dummy

        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = ListNode(l1.val)
                l1=l1.next
            else:
                dummy.next = ListNode(l2.val)
                l2 = l2.next
            dummy = dummy.next

        if l1:
            dummy.next = l1

        if l2:
            dummy.next = l2

        return new_head.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left = head
        
        right = self.getMid(head)
        temp = right.next
        right.next = None

        right = temp

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left,right)



    

