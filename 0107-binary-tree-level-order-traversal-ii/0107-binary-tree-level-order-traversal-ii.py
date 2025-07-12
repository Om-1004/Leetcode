# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque()        
        queue.append(root)
        ans = deque()

        while queue:
            levelSize = len(queue)
            levelArr = []
            for _ in range(levelSize):
                node = queue.popleft()
                levelArr.append(node.val)

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)
            
            ans.appendleft(levelArr)
        
        return list(ans)

