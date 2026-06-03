# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
solution:
- define an array
- go through all the nodes in the tree
- put the values into the array
- sort the array afterwards then
'''

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        array = []

        def dfs(node, array):

            if not node:
                return
            
            array.append(node.val)
            dfs(node.left, array)
            dfs(node.right, array)

            array.sort()
        
            return array
        
        result = dfs(root, array)

        return result[k - 1]
        
        
            
            
            

            

            

            

            

            

            

            

            

            

            

            

            






















































        






        