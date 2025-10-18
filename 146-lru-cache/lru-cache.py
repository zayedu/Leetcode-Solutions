class Node:
    def __init__ (self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}

        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)

        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]

        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = self.head.next
        self.head.next = node
        node.next.prev = node 
        node.prev = self.head
        self.map[key] = node
        return self.map[key].val

    def put(self, key: int, value: int) -> None:

        if key not in self.map and len(self.map) == self.capacity:
            # eject LRU element

            last_node = self.tail.prev
            key_to_delete = last_node.key
            last_node.prev.next = self.tail
            self.tail.prev = last_node.prev

            del self.map[key_to_delete]
        
        if key in self.map:

            node = self.map[key]

            node.prev.next = node.next
            node.next.prev = node.prev

        node = Node(key,value)
        node.next = self.head.next
        node.prev= self.head

        node.next.prev =node
        self.head.next = node

        self.map[key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)