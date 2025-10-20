class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.vals_map = {}

    def insert(self, val: int) -> bool:
        if val in self.vals_map:
            return False

        self.vals.append(val)
        self.vals_map[val] = len(self.vals)-1
        return True

    def remove(self, val: int) -> bool:
        
        if val not in self.vals_map:
            return False

        if val == self.vals[-1]:
            del self.vals_map[val]
            self.vals.pop()
            return True

        index_to_replace = self.vals_map[val]
        self.vals[index_to_replace] = self.vals[-1]
        self.vals.pop()
        self.vals_map[self.vals[index_to_replace] ] = index_to_replace
        del self.vals_map[val]

        return True
        
    
    def getRandom(self) -> int:
        
        return self.vals[randint(0,len(self.vals)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()