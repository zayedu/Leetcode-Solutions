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
        if not node:
            return None


        while node:
            if node.child:

                temp = node.next
                child = node.child
                node.child = None

                next_node = self.flatten(child)
                next_node.prev = node
                node.next = next_node

                while node.next:
                    node = node.next

                node.next = temp
                if node.next:
                    node.next.prev= node

            node = node.next

        return head