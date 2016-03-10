# Given a binary tree, find its maximum depth. The maximum depth 
# is the number of nodes along the longest path from the root 
# node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
            
        depth = 1
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        if left >= right:
            return depth + left
        else:
            return depth + right

