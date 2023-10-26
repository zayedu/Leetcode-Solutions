# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        prev = None
        cur=head
        nxt=head.next

        while cur!= None:
            nxt=cur.next

            cur.next=prev
            prev=cur
            cur=nxt

        head = prev
        return head
