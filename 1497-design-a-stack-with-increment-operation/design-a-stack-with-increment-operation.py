class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        self.increment_amount = []        

    def push(self, x: int) -> None:
        if len(self.stack) == self.maxSize:
            return

        self.stack.append(x)
        self.increment_amount.append(0)

    def pop(self) -> int:
        # print(self.stack,self.increment_amount)
        if not self.stack:
            return -1

        index = len(self.stack) - 1
        increment = self.increment_amount[index]

        if index>0:
            self.increment_amount[index-1] += increment
        self.increment_amount.pop()
        return self.stack.pop() + increment

    def increment(self, k: int, val: int) -> None:
        if not self.stack:
            return
        index = min(k,len(self.stack)) -1
        self.increment_amount[index] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# obj.pop()
# obj.increment(k,val)