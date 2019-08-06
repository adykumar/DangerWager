"""
155. Min Stack
Easy

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""

"""
Time- constant for every operation
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack= []
        self.minpos= 0


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        top= len(self.stack)
        if top==0:
            self.stack.append((x, 0))
        elif x < self.stack[self.minpos][0]:
            self.stack.append((x, self.minpos))
            self.minpos= top
        else:
            self.stack.append((x, top))


    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack)>0:
            if self.minpos==len(self.stack)-1:
                self.minpos= self.stack[-1][1]
            self.stack.pop()


    def top(self):
        #print "top",
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack)==0: return
        return self.stack[self.minpos][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
