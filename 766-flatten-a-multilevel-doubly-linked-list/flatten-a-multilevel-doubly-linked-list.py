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

                temp = node.next
                
                next_node = self.flatten(node.child)
                node.child = None
                next_node.prev= node
                node.next = next_node

                while node.next:
                    node = node.next
                if temp:
                    temp.prev= node
                node.next = temp

            else:
                node= node.next

        return head