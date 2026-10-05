class MinStack:

    def __init__(self):
        self.obj = deque()
        self.minobj = float('inf')
        self.prior = deque()

    def push(self, val: int) -> None:
        if val<=self.minobj:
            self.prior.append(self.minobj)
            self.minobj = val
        self.obj.append(val)

    def pop(self) -> None:
        pop = self.obj.pop()
        if pop == self.minobj:
            self.minobj = self.prior.pop()

    def top(self) -> int:
        top =  self.obj[-1]
        return top

    def getMin(self) -> int:
        return self.minobj
        
