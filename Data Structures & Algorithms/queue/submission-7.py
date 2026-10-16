class Node:
    def __init__(self, value):
        self.current = value
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.first = None
        self.last = None

    def isEmpty(self) -> bool:
        if self.first == None:
            return True
        return False

    def append(self, value: int) -> None:
        newNode = Node(value) # Create new node

        # First Node
        if self.last == None:
            self.first = newNode
            self.last = newNode
            return

        self.last.next = newNode
        newNode.prev = self.last
        self.last = newNode

    def appendleft(self, value: int) -> None:
        newNode = Node(value)
        if self.first != None:
            self.first.prev = newNode
            newNode.next = self.first
            self.first = newNode

        if self.first == None:
            self.first = newNode
            self.last = newNode

    def pop(self) -> int:
        if self.last:
            if self.last is self.first:
                value = self.last.current
                self.first = None
                self.last = None
                return value
            value = self.last.current
            self.last = self.last.prev
            self.last.next = None
            return value
        return -1

    def popleft(self) -> int:
        if self.first:
            if self.last is self.first:
                value = self.last.current
                self.first = None
                self.last = None
                return value
            value = self.first.current
            self.first = self.first.next
            return value
        return -1
