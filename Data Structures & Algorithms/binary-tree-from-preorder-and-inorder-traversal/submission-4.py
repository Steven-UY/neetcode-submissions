# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
preorder: first element is the root
inorder: the left subtree is to the left of the root, right subtree is to the right

we must determine where the root is in inorder

edge case:
- there is no inorder and preorder lists

1. we get the root that we need
2. root is the middle term in inorder
3. we repeat the process for the left and right sides of the inorder? this would be part
of the recursive solution
'''

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder and not inorder:
            return None
        
        root = TreeNode(preorder[0]) 
        mid = inorder.index(preorder[0])

        #recursively build up the solution
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1: ], inorder[mid+1:])

        return root









        

        

        

        

        


