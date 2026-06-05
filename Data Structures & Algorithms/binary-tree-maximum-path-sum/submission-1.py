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

        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            res[0] = max(res[0], root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]
            
           

# have a feeling that we aren't actually traversing the tree
            









        









