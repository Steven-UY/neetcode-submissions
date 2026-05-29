# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
if it's a bst return True else return False

bst:
- left node less than parent
- right node greater than parent

subproblem is to check these conditions to the current node

        5
       / \
      4   6
         / \
        3   7

keep track of some upper and lower bound
lower bound should be the root (right)
upper bound should be the root (left)
above are the only important things to keep in mind
'''


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, low, high):

            if not node:
                return True
            
            if not (low < node.val < high):
                return False
        
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        
        return dfs(root, float('-inf'), float('inf'))



        











