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
    def flatten(self, head: "Optional[Node]") -> "Optional[Node]":
        node = head

        def dfs(node, torso):

            if node.child != None:
            
                tor = node.next
                node.next = node.child
                node.child.prev = node
                node.child = None
                dfs(node.next, tor)

            if node.next == None:
                if torso is not None:
                    node.next = torso
                    torso.prev = node
                
                return

            else:
                dfs(node.next, torso)

        while node:

            if node.child != None:
                torso = node.next
                node.next = node.child
                node.child.prev = node
                node.child = None
                dfs(node.next, torso)

            node = node.next

        return head
