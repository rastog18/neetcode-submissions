class Node:
    def __init__(self, key, val=0, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.occupied = 0
        self.adjList = {}
        self.head = Node(-1, -1, None, None)
        self.tail = Node(-2, -1, None, self.head)
        self.head.next = self.tail

    def removeNode(self, node: Node) ->None:
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None

    def addToHead(self, node: Node) -> None:
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head

    def get(self, key: int) -> int:
        # remove node from the current position
        # add node to the head of the linkedList
        node = self.adjList.get(key)
        if node:
            self.removeNode(node)
            self.addToHead(node)
            return node.val
        
        return -1

    def put(self, key: int, value: int) -> None:
        # update value and move node to the head of the linkedList
        # if full create new node, delete last node and move node to head of linkedList
        # create new node and move node to head of linkedList
        node = self.adjList.get(key)
        if node:
            node.val = value
            self.removeNode(node)
            self.addToHead(node)
        else:
            if self.occupied == self.capacity:
                curTail = self.tail.prev
                self.removeNode(curTail)
                self.adjList.pop(curTail.key)
                
            else:
                self.occupied += 1
    
            node = Node(key, value)
            self.addToHead(node)
            self.adjList[key] = node
        
        
