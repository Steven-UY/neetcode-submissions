# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
- so we can do bfs but just get the last element of each level since it will be "seen" on the right-hand
side then
- so level order traversal but extract the last term in the sublist
'''

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []

            #add left and right children
            for i in range(qLen):
                #extract the current node from q
                node = q.popleft()
                #add current node to level and add children to the q
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            #check if the level in the tree actually exists and insert it then
            if level:
                res.append(level[-1])
        
        print(res)
        return res








            





                




        















        
