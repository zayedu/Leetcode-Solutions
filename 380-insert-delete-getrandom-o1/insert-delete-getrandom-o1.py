import random
import heapq  # if you had this elsewhere; harmless to leave/remove

class RandomizedSet:

    def __init__(self):
        self.size = 0
        self.values = []
        self.values_map = {}

    def insert(self, val: int) -> bool:
        if val in self.values_map:
            return False
        self.values.append(val)
        self.size += 1

        self.values_map[val] = self.size - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.values_map:
            return False

        idx = self.values_map[val]
        
        last_val = self.values[self.size - 1]

        if idx != self.size-1:
            self.values[idx] = last_val
            self.values_map[last_val] = idx
 
        self.values.pop()
        self.size -= 1
        del self.values_map[val]
        return True

    def getRandom(self) -> int:
        random_index = random.randint(0, self.size - 1)
        return self.values[random_index]
