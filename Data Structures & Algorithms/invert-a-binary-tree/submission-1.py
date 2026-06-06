# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def swap(self, node: Optional[TreeNode]):
        if not node:
            return None

        if node.left and node.right:
            node.left, node.right = self.swap(node.right), self.swap(node.left)
        elif node.left and not node.right:
            node.left, node.right = None, self.swap(node.left)
        else:
            node.left, node.right = self.swap(node.right), None

        return node

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        return self.swap(root)
