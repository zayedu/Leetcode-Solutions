class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = { }
        '''
        key -> Node
        '''
        self.head = Node(-1,-1)
        

        self.tail = Node(-1,-1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:

        if key in self.cache:
            
            self.cache[key].prev.next = self.cache[key].next
            self.cache[key].next.prev = self.cache[key].prev

            self.cache[key].next = self.head.next
            self.cache[key].prev = self.head

            self.head.next.prev = self.cache[key]
            self.head.next = self.cache[key]

            return self.cache[key].value
        
        return -1


    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.cache[key].value = value
            
            self.cache[key].prev.next = self.cache[key].next
            self.cache[key].next.prev = self.cache[key].prev

            self.cache[key].next = self.head.next
            self.cache[key].prev = self.head

            self.head.next.prev = self.cache[key]
            self.head.next = self.cache[key]

            return

        if len(self.cache) >= self.capacity:
            key_to_delete = self.tail.prev.key

            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail

            del self.cache[key_to_delete]

        value_holding_node = Node(key, value)

        value_holding_node.next = self.head.next
        value_holding_node.prev = self.head

        self.head.next.prev = value_holding_node
        self.head.next = value_holding_node

        self.cache[key] = value_holding_node


            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)