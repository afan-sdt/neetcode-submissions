class MinStack:

    def __init__(self):
        self.stck = []
        self.minElement = float('inf')
        # i think i need a last min so when we pop we know what to go back to
        # should store a tuple, element, lastMinWhenAdded
    def push(self, val: int) -> None:
        self.stck.append((val, self.minElement))
        self.minElement = min(self.minElement, val)

    def pop(self) -> None:
        self.minElement = self.stck.pop()[1]

    def top(self) -> int:
        return self.stck[-1][0]

    def getMin(self) -> int:
        return self.minElement
