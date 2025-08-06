# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0  

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.diameter

    def helper(self, node):
        if not node:
            return 0  

        left_height = self.helper(node.left)
        right_height = self.helper(node.right)

        self.diameter = max(self.diameter, left_height + right_height)
        return 1 + max(left_height, right_height)
