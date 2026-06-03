# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
build a binary tree from a preoder traversal array and an inorder traversal

preorder: root is always the first in the array
inorder: tells us what is in the left and right subtrees

this is important because in order to build the tree it's important to know where the root is
and what/where the left and right subtrees are

recursively run the process on the left and right subtrees
'''

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not inorder or not preorder:

            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1: ])

        return root

        

        

        

        

        

        

        
        

        

        

        



        

        

        

        

        

        

        

        
        

        















































































        