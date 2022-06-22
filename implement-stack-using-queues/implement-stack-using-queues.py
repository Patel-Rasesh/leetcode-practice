class MyStack(object):

    def __init__(self):
        self.myStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.myStack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        return self.myStack.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        return self.myStack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.myStack) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()