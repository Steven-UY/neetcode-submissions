# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string
    # traverse and put into the array using level order traversal
    '''
    Level order traversal:
    - node in the queue then we add left and right nodes
    - pop and then add the children
    - continue this while the queue is not empty
    '''
    from collections import deque

    def serialize(self, root: Optional[TreeNode]) -> str:

        result = []
        
        queue = deque([root])

        while queue:
            current  = queue.popleft()
            
            if current:
                result.append(str(current.val))
                queue.append(current.left)
                queue.append(current.right)
            else:
                result.append("None")
        
        return ",".join(result)

    # Decodes your encoded data to tree
    '''
    [1, 2, 3, null, null, 4, 5]

    Take the first node and attach its left and right children
    repeat until 
    '''
    def deserialize(self, data: str) -> Optional[TreeNode]:

        values = data.split(",")

        if values[0] == "None":
            return None

        root = TreeNode(int(values[0]))
        queue = deque([root])

        #we want to have the root in the queue
        #pop the node off of the queue
        #add the popped node to the tree
        #add its children to the queue
        #repeat this process until we reach the end of the serialized string
        #increase index whenever we add something to the queue

        index = 1

        while queue:
            current = queue.popleft()

            if values[index] != "None":
                current.left = TreeNode(int(values[index]))
                queue.append(current.left)
            index += 1

            if values[index] != "None":
                current.right = TreeNode(int(values[index]))
                queue.append(current.right)
            index += 1
                
        return root














            














































































