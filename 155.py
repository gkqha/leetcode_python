class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.mins = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.items.append(x)
        if self.mins == [] or x <= self.mins[-1]:
            self.mins.append(x)

    def pop(self):
        """
        :rtype: void
        """
        tmp = self.items[-1]
        self.items.pop()
        if tmp==self.mins[-1]:
            self.mins.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.items[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.mins[-1]
m=MinStack()
m.push(-2)
m.push(0)
m.push(-3)
m.pop()
print(m.getMin())