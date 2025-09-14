# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        col_map = defaultdict(list)  # col -> values in top-to-bottom, left-to-right order
        q = deque([(root, 0)])
        min_c = max_c = 0

        while q:
            node, c = q.popleft()
            col_map[c].append(node.val)
            min_c = min(min_c, c)
            max_c = max(max_c, c)

            if node.left:
                q.append((node.left, c - 1))
            if node.right:
                q.append((node.right, c + 1))

        return [col_map[c] for c in range(min_c, max_c + 1)]