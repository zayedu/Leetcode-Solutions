class Node:

    def __init__(self, key:int=-1, val:int=-1):
        self.key = key
        self.val = val
        self.next: Node = None
        self.prev: Node = None

class LRUCache:

    def __init__(self, capacity: int):
        self.nodes: dict = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        
        if key not in self.nodes:
            return -1

        node = self.nodes[key]

        #mutate DLL

        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = self.head
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self.nodes[key].val = value
            self.get(key)
            return

        node = Node(key,value)
        
        #eject
        while len(self.nodes) >= self.capacity:
            eject = self.tail.prev
            eject.prev.next = self.tail
            self.tail.prev = eject.prev
            del self.nodes[eject.key]

        self.nodes[node.key] = node
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)