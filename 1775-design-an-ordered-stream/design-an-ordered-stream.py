class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.values = [False] * n
        self.pointer = 0
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.values[idKey-1] = value

        continuous_chunk = [ ]
        
        while self.pointer < self.n and self.values[self.pointer]:
            continuous_chunk.append(self.values[self.pointer])
            self.pointer+=1
        return continuous_chunk
        
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)