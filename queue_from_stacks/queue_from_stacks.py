# Author:      Jacob Moore
# Date:        7/24/22
# Description: This program implements a queue using two stacks
#              which are implemented using arrays. This code is all
#              my own

class MyQueue(object):

    def __init__(self):
        self.stack = []
        self.temp_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        while self.stack:
            self.temp_stack.append(self.stack.pop())
        self.stack.append(x)
        while self.temp_stack:
            self.stack.append(self.temp_stack.pop())
        return

    def pop(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return self.stack.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return self.stack[len(self.stack) - 1]

    def empty(self):
        """
        :rtype: bool
        """
        if self.stack:
            return False
        else:
            return True

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
