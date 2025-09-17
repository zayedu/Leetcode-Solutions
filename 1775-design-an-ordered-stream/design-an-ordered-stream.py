class OrderedStream:

    def __init__(self, n: int):
        self.pointer = 1
        self.map = { }

    def insert(self, idKey: int, value: str) -> List[str]:
        
        self.map[idKey] = value
        ans = []
        while self.pointer in self.map:
            ans.append(self.map[self.pointer])

            self.pointer += 1

        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)