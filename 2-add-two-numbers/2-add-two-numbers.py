# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def process_list(l):
            temp = l
            number = 0
            multiplier = 1
            while temp is not None:
                number += temp.val*multiplier
                temp = temp.next
                multiplier *= 10
            return number
        
        def makelist(number):
            listNum = list(str(number))[::-1]
            # ['7','0','8']
            numLength = len(listNum)
            nodes = []
            index = 0
            while numLength != 0:
                nodes.append(ListNode(int(listNum[index])))
                index += 1
                numLength -= 1
                
            print(nodes)    # Sanity check
            if nodes:
                head = nodes.pop(0)
            else:
                head = None
            temp = head
            while nodes:
                temp.next = nodes.pop(0)
                temp = temp.next
            return head
            
        resultNumber = process_list(l1) + process_list(l2)
        return makelist(resultNumber)