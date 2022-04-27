# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def isSame(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            elif p.val == q.val:
                return True
            else:
                return False
        
        recursionStack = deque([(p,q)])
        while recursionStack:
            p, q = recursionStack.popleft()
            if not isSame(p, q):
                return False
            
            if p or q:
                recursionStack.append((p.left, q.left))
                recursionStack.append((p.right, q.right))
            
        return True
        
        
        