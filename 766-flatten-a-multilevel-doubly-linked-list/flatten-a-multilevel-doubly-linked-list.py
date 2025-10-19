"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node = head

        while node:

            if node.child:

                next_node  = node.next

                node.next = self.flatten(node.child)
                node.child = None
                node.next.prev = node

                while node.next:
                    node = node.next

                node.next= next_node
                if node.next:
                    node.next.prev = node
            node = node.next

        return head
