# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is not None:
            result = [[root.val]]
        else:
            return []
        parentNodes, childNodes = [], []
        parentNodes.append(root)
        isOrdered = False
        while parentNodes:
            for eachParent in parentNodes:
                if eachParent.left is not None:
                    childNodes.append(eachParent.left)
                if eachParent.right is not None:
                    childNodes.append(eachParent.right)
            if isOrdered:
                levelNodes = []
                for index in range(len(childNodes)):
                    levelNodes.append(childNodes[index].val)
                isOrdered = False
            else:
                levelNodes = []
                for index in range(len(childNodes)-1, -1, -1):
                    levelNodes.append(childNodes[index].val)
                isOrdered = True
            if levelNodes:
                result.append(levelNodes)
            parentNodes = childNodes
            childNodes = []
            
        return result