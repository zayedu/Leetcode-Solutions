class RandomizedSet:

    def __init__(self):
        self.map = { }
        '''
        val -> idx
        '''
        self.values = []
    def insert(self, val: int) -> bool:
        present = val in self.map
        if present:
            return not present
        self.values.append(val)
        self.map[val] = len(self.values)-1
        return not present

    def remove(self, val: int) -> bool:
        present = val in self.map

        if not present:
            return present

        index = self.map.get(val)
        temp = self.values[-1]
        self.values[index] = temp

        if temp != val:
            self.map[temp] = index

        del self.map[val]

        self.values.pop()
        return present
    def getRandom(self) -> int:
        random_index = random.randint(0,len(self.values)-1)
        return self.values[random_index]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()