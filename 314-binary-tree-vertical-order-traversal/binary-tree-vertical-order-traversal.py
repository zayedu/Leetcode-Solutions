# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        vert_ordered_nodes = defaultdict(list)

        queue = deque([[root,0]])

        while queue:
            node,col = queue.popleft()

            vert_ordered_nodes[col].append(node.val)

            if node.left:
                queue.append([node.left,col-1])

            if node.right:
                queue.append([node.right,col+1])


        index = min(vert_ordered_nodes.keys())
        vertical_traversal_order = []
        while index in vert_ordered_nodes:
            vertical_traversal_order.append(vert_ordered_nodes[index])
            index += 1

        return vertical_traversal_order
