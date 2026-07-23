class MinStack:

    def __init__(self):
        self.nums = []
        self.min = 0

    def push(self, val: int) -> None:
        prev = self.min
        if not self.nums or self.min > val:
            self.min = val
        self.nums.append((val, prev))
        

    def pop(self) -> None:
        temp = self.nums.pop()
        self.min = temp[1]

    def top(self) -> int:
        return self.nums[-1][0]
        

    def getMin(self) -> int:
        return self.min
        
