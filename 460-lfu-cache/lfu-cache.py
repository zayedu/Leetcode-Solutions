class ListNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        self.uses = 1

class DoublyLinkedList:
    def __init__(self, key):
        self.key = key
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.dummy = self.head
        self.size = 0

    def append(self,node):

        node.prev = self.tail.prev
        node.next = self.tail

        node.prev.next = node
        node.next.prev = node
        self.size +=1

        return node
        
    def pop(self,node):
        next_node = node.next
        node.next.prev = node.prev
        node.prev.next = node.next
        self.size -= 1
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.nodes = {}

        self.use_count = {}
        self.capacity = capacity
        

    def get(self, key: int) -> int:

        if key not in self.nodes:
            return -1

        node = self.nodes[key]
        self.use_count[node.uses].pop(node)

        node.uses += 1
        if node.uses in self.use_count:
            self.use_count[node.uses].append(node)
        else:
            self.use_count[node.uses] = DoublyLinkedList(node.uses)
            self.use_count[node.uses].append(node)

        if self.use_count[node.uses-1].size == 0:
            del self.use_count[node.uses-1]

        return node.val

    def put(self, key: int, value: int) -> None:

        if key not in self.nodes and len(self.nodes) == self.capacity:
            # eject

            min_uses = min(self.use_count.keys())

            min_used = self.use_count[min_uses]

            evict = min_used.pop(min_used.head.next)
            del self.nodes[evict.key]
            if min_used.size == 0:
                del self.use_count[min_uses]

        node = ListNode(key,value)

        if key in self.nodes:
            node = self.nodes[key]

            self.use_count[node.uses].pop(node)
            
            if self.use_count[node.uses].size == 0:
                del self.use_count[node.uses]

            node.uses += 1
            node.val = value
        if node.uses not in self.use_count:
            self.use_count[node.uses] = DoublyLinkedList(node.uses)
        self.use_count[node.uses].append(node)
        self.nodes[key] = node




        

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)