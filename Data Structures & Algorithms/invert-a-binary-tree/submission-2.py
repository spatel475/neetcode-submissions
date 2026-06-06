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

        node.left, node.right = self.swap(node.right), self.swap(node.left)

        return node

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        return self.swap(root)
