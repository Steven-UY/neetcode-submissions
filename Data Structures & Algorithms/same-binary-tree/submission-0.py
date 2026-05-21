# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
- traverse through each tree
- collect an array of nodes
- if the arrays match then it's equivalent
'''


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(root, array):

            if not root:
                array.append(None)
                return
            
            array.append(root.val)
            dfs(root.left, array)
            dfs(root.right, array)

            return array
        
        tree_1 = dfs(p, [])
        tree_2 = dfs(q, [])

        if tree_1 == tree_2:
            return True
        else:
            return False







            

            

            




            
            
            

            

            

            




