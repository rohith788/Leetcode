class MinStack:
    def __init__(self):
        self.arr = []
        self.min = []
        
    def push(self, x: int) -> None:
        if len(self.min) == 0:self.min.append(x)
        elif self.min[-1] >= x: self.min.append(x)
        self.arr.append(x)

    def pop(self) -> None:
        if self.min[-1] == self.arr[-1]: self.min = self.min[:-1]
        self.arr = self.arr[:-1]

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min[-1] if len(self.min) > 0 else 0


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()