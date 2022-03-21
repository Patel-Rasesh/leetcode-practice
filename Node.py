class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class LinkedList:
    linearList = []
    def printList(self, head):
        temp = head
        while temp:
            print(temp.val, end = " ")
            temp = temp.next
    def makeAnArray(self, head):
        temp = head
        while temp:
            self.linearList.append(temp.val)
        return self.linearList
    def detectCycle(self, runner1, runner2):
        if runner2 == None:
            return False
        if(runner1 == runner2):
            return True
        return self.detectCycle(runner1.next, runner2.next.next)

head = Node(10)
neck = Node(20)
torso = Node(30)
body = Node(40)
legs = Node(50)
head.next = neck
neck.next = torso
torso.next = body
body.next = legs
legs.next = head
obj = LinkedList()
#print("Printing LinkedList ...")
#print(obj.printList(head))
# if obj.detectCycle(head, head.next):
#     print("Cycle is detected")
# else:
#     print("No cycle")
obj.makeAnArray(head)
print(obj.linearList)
