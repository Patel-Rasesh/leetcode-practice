#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def printTree(self, root):
        if root == None:
            return
        self.printTree(root.left)
        print(root.val, " ", end = " ")
        self.printTree(root.right)
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        elif root.left and root.right:
            # Swap right and left children
            root.left, root.right = root.right, root.left
            left = self.invertTree(root.left)
            if not left:
                return self.invertTree(root.right)
        elif root.left:
            root.left, root.right = None, root.left
            return self.invertTree(root.right)
        elif root.right:
            root.right, root.left = None, root.left
            return self.invertTree(root.left)
        else:
            return root

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
rootNode = Solution()
print(rootNode.printTree(root))
print(rootNode.invertTree(root))
