class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def printTree(root, arrayForm):
    if(root == None):
        return
    printTree(root.left, arrayForm)
    arrayForm.append(root.val)
    # print(root.val, end=' ')
    printTree(root.right, arrayForm)

# Tree 1
root1 = Node(0)
node11 = Node(-10)
node12 = Node(10)
root1.left = node11
root1.right = node12
global arrayForm1, arrayForm2
arrayForm1, arrayForm2 = [], []
printTree(root1, arrayForm1)
print("-------")
print(arrayForm1)
# Tree 2
root2 = Node(5)
node21 = Node(1)
node22 = Node(7)
node23 = Node(0)
node24 = Node(2)
root2.left = node21
root2.right = node22
node21.left = node23
node21.right = node24
printTree(root2, arrayForm2)
print()
print("-----------")
print(arrayForm2)

def twoSumBSTs(root1, root2, target):
    if root1 is None or root2 is None:
        return False
    if root1.val + root2.val == target:
        return True
    if root1.val + root2.val < target:
        if(root1.val < target and root2.val < target):
            return twoSumBSTs(root1.right, root2.right, target)
        else:
            temp = twoSumBSTs(root1, root2.right, target)
            if temp is False:
                return twoSumBSTs(root1.right, root2, target)
            return temp
    else:
        if(root1.val > target and root2.val > target):
            return twoSumBSTs(root1.left, root2.left, target)
        else:
            temp = twoSumBSTs(root1, root2.left, target)
            if temp is False:
                return twoSumBSTs(root1.left, root2, target)
            return temp

arrayForm1 = [17-node for node in arrayForm1]
print("Printing complements")
print(arrayForm1)

for node1 in arrayForm1:
    for node2 in arrayForm2:
        if node1==node2:
            pass


