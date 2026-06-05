# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
return the max path sum
start from every single node
should consider a max value per path


constraints:
there's always at least one node

subproblem:
is the sum of the current path greater than max?
- if yes: the sum of that path becomes max
- if no: the max value remains as it is
- go left and right
- return max by the end

if we hit any null we just do an empty return
'''

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.best = float('-inf')   # the answer; any node could be the bend point

        def dfs(node):
            if not node:
                return 0

            # best downward gain from each side; clamp negatives to 0
            # (a negative branch is never worth including — skip it)
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # path that BENDS here, using both children. record but don't return it.
            self.best = max(self.best, node.val + left + right)

            # what we hand UP: straight line through one side only
            return node.val + max(left, right)

        dfs(root)
        return self.best
            
           

# have a feeling that we aren't actually traversing the tree
            









        









