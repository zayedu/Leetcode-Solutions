import random
class RandomizedSet:

    def __init__(self):
        self.inventory_map = { }
        self.inventory_list = [ ]
        self.inventory_size = 0

    def insert(self, val: int) -> bool:
        exists = val in self.inventory_map

        if not exists:
            self.inventory_size += 1
            self.inventory_list.append(val)
            self.inventory_map[val] = self.inventory_size-1
        
        return not exists


    def remove(self, val: int) -> bool:
        exists = val in self.inventory_map

        if exists:
            if self.inventory_map[val] == self.inventory_size - 1:
                del self.inventory_map[val]
                self.inventory_size -= 1
                self.inventory_list.pop()
                return exists

            self.inventory_size -= 1
            replace_with = self.inventory_list.pop()

            to_replace = self.inventory_map[val]

            self.inventory_list[to_replace] = replace_with

            self.inventory_map[replace_with] = to_replace
            del self.inventory_map[val]

        return exists


    def getRandom(self) -> int:
        random_idx = random.randint(0,self.inventory_size-1)

        return self.inventory_list[random_idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()