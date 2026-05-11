# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
tp:
- dfs and increase counter as we go down
- keep this length value to be a maximum value
- then we return the depth
'''


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node, depth):

            if not node:
                return depth
            #traverse
            dfs(node.left, depth + 1)
            left = dfs(node.left, depth + 1)
            right = dfs(node.right, depth + 1)
            
            return max(left, right)


        return dfs(root, 0)