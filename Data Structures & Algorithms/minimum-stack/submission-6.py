class MinStack:

    def __init__(self):
        self.mins = []
        self.stack = []
        self.ans = None
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.ans is None or val <= self.ans:
            self.mins.append(val)
            self.ans = val

    def pop(self) -> None:
        removed = self.stack.pop()
        if removed == self.mins[-1]:
            self.mins.pop()
            if self.mins:
                self.ans = self.mins[-1]
            else:
                self.ans = None
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.ans
