class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = list()
        self.stack_helper = list()

    def __str__(self):
        return f"{self.stack}"

    def move_queue(self):
        if not self.stack_helper:
            while self.stack:
                last_entry = self.stack.pop()
                self.stack_helper.append(last_entry)

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        self.move_queue()

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.move_queue()
        
        return self.stack_helper.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self.move_queue()

        # return the front element
        return self.stack_helper[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if not self.stack and self.stack_helper:
            return print(True)
        return print(False)

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
# obj.push(x)
obj.push(18)
obj.push(9)
obj.push(27)
obj.push(39)

param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()

print(param_2)
print(param_3)
print(param_4)