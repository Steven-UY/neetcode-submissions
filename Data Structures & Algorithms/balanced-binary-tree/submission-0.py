# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
a binary tree is balanced if the height on either subtree doesn't differ
by more than 1

get the left and right heights and subtract. if the difference is more than
absolute value of 1 then we return False, else we return True

note it must be calculated for each node 
'''

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):

            if not root:
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]


            









        
        
        


            

        




            





        
         
        















