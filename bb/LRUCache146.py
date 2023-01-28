class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.tail, self.head = Node(0, 0), Node(0,0)
        self.cache = {} # key:Node
        self.tail.next, self.head.prev = self.head, self.tail

    def insert(self, node): #  prev node head
        prev = self.head.prev
        prev.next = node
        node.prev = prev

        self.head.prev = node
        node.next = self.head

        self.cache[node.key] = node
        
    
    def remove(self, node):#  prev node next
        prev, next = node.prev, node.next 
        prev.next = next
        next.prev = prev

        del self.cache[node.key]
    
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.insert(Node(key, value))
        if len(self.cache) > self.capacity:
            self.remove(self.tail.next)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)