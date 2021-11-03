class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

class LinkedList:
    def __init__(self):
        self.headval = None
    
    def printList(self):
        printNode = self.headval
        while printNode is not None:
            print(printNode.dataval)
            printNode = printNode.nextval

listOne = LinkedList()
listOne.headval = Node(12)
nodeTwo = Node(14)
nodeThree = Node(16)

listTwo = LinkedList()
listTwo.headval = Node(13)
nodeFour = Node(15)
nodeFive = Node(17)
nodeSix = Node(0)

listOne.headval.nextval = nodeTwo
nodeTwo.nextval = nodeThree
nodeThree.nextval = nodeSix

listTwo.headval.nextval = nodeFour
nodeFour.nextval = nodeFive
nodeFive.nextval = nodeSix

listThree = LinkedList()
def compareSortedLinkedList(listOne, listTwo):
    global listThree
    tempOne = listOne.headval
    tempTwo = listTwo.headval
    print(tempOne.nextval.nextval.dataval)
    print(tempTwo.dataval)
    #print(tempTwo.nextval.nextval.nextval.nextval.dataval)
    print(tempTwo.nextval.nextval.nextval.dataval)
    if(tempOne.dataval <= tempTwo.dataval):
        listThree.headval = Node(tempOne.dataval)
        tempOne = tempOne.nextval
    else:
        listThree.headval = Node(tempTwo.dataval)
        tempTwo = tempTwo.nextval
    print(tempOne.nextval.dataval)
    print(tempTwo.nextval.dataval)
    while(tempOne.nextval.dataval != 0 or tempTwo.nextval.dataval != 0):
        if(tempOne.nextval.dataval == 0):
            listThree.nextval = Node(tempTwo.dataval)
        elif(tempTwo.nextval.dataval == 0):
            listThree.nextval = Node(tempOne.dataval)
        elif(tempOne.dataval <= tempTwo.dataval):
            listThree.nextval = Node(tempOne.dataval)
            tempOne = tempOne.nextval
        else:
            listThree.nextval = Node(tempTwo.dataval)
            tempTwo = tempTwo.nextval

compareSortedLinkedList(listOne, listTwo)
listThree.printList()
