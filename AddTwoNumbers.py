class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None

    def insertLinkedList(self, node):
        newNode = ListNode(node)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def printLinkedList(self):
        if(self.head):
            current = self.head
            while(current):
                print(current.val)            
                current = current.next
        else:
            print("Empty Linked List")

    def addTwoNumbers(self, l1, l2):
            node1 = ListNode()
            node2 = ListNode()
            nodeTotal = ListNode()
            node1 = l1.head
            node2 = l2.head
            while(node1  or node2):
                if(node1.val + node2.val >= 10):
                    nodeTotal.val += (node1.val + node2.val)%10
                    nodeTotal.next = ListNode(1)
                else:
                    nodeTotal.val += (node1.val + node2.val)
                    nodeTotal.next = ListNode(0)
                node1 = node1.next
                node2 = node2.next
                nodeTotal = nodeTotal.next
            return nodeTotal
            
l1 = LinkedList()
l1.insertLinkedList(2)
l1.insertLinkedList(3)
l1.insertLinkedList(4)

l2 = LinkedList()
l2.insertLinkedList(2)
l2.insertLinkedList(3)
l2.insertLinkedList(4)

sumLinkedList = LinkedList()
sumLinkedList.addTwoNumbers(l1, l2)

sumLinkedList.printLinkedList()