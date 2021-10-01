class MaxStack(list):
    def push(self, x):
        m = max(x, self[-1][1] if self else x)
        self.append((x, m))

    def pop(self):
        return list.pop(self)[0]

    def top(self):
        return self[-1][0]

    def peekMax(self):
        return self[-1][1]

    def popMax(self):
        b = []
        while self.top() != self.peekMax():
            b.append(self.pop())

        r = self.pop()
        while b:
            self.push(b.pop())
        return r


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

