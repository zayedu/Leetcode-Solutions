"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        def next_node(node):

            while node:
                if node.left:
                    return node.left

                if node.right:
                    return node.right

                
                node = node.next

            return None

        def attach(node):

            if not node:
                return

            if node.left:
                node.left.next = node.right if node.right else next_node(node.next)

            if node.right:
                node.right.next = next_node(node.next)

            attach(node.right)
            attach(node.left)
            

        attach(root)

        return root