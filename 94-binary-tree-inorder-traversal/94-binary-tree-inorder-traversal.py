# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 1. Go left until you cannot, and append that node to the output
        tempNode = root
        inorderOutput = []
        if not tempNode:
            return []
        stack = []
        while tempNode or stack:
            while tempNode:
                stack.append(tempNode)
                tempNode = tempNode.left
            tempNode = stack.pop(-1)
            inorderOutput.append(tempNode.val)

            # 2. Move one right, and repeat step 1 from that node
            tempNode = tempNode.right
        
        return inorderOutput