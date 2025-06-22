# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def findHeight(root):
            if root is None:
                return 0

            if root.left is None and root.right is None:
                return 1
            else:
                return 1 + max(findHeight(root.left), findHeight(root.right))

            
        leftSubTreeHeight = findHeight(root.left)
        rightSubTreeHeight = findHeight(root.right)

        if abs(leftSubTreeHeight - rightSubTreeHeight) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
