# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if (
            (root1 and root2)
            and root1.val == root2.val
            and self.isSameTree(root1.left, root2.left)
            and self.isSameTree(root1.right, root2.right)
        ):
            return True
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root and subRoot:
            isSubRootOfSelf = self.isSameTree(root, subRoot)
            isSubRootOfLeft = self.isSubtree(root.left, subRoot)
            isSubRootOfRight = self.isSubtree(root.right, subRoot)
            return isSubRootOfSelf or isSubRootOfLeft or isSubRootOfRight
        return False
