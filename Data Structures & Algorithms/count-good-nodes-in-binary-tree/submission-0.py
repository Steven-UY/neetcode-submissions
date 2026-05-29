# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
good path: root of tree to node x where there are no nodes in between greater than x node val

dfs and we should keep a maximum value of what we've already traversed, if the current node is
greater its good

have some global variable that counts the number of "good" or acceptable nodes
'''

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        good_nodes = 0

        #early stopping condition
        if not root:
            return 0

        def dfs(node, biggest_node):
            nonlocal good_nodes

            if not node:
                return 0
            
            #current problem: is the current node a good node?
            if node.val >= biggest_node:
                biggest_node = node.val
                good_nodes += 1
            
            dfs(node.left, biggest_node)
            dfs(node.right, biggest_node)

            return good_nodes

        return dfs(root, root.val)
        

            

            
            
            

            

            

            

            























                









            




            












            

            

            
        

        









        