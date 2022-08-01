class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.next = next
        self.value = value
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._len = 0

    def __len__(self):
        return self._len

    def _traverseToPosition(self, position: int):
        i = 0
        curr = self.head
        while i != position:
            curr = curr.next
            i += 1
        return curr

    def append(self, val):
        new_node = Node(val, prev=self.tail)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._len += 1

    def prepend(self, val):
        new_node = Node(val, self.head)
        self.head.prev = new_node
        self.head = new_node
        self._len += 1

    def insert(self, position, val):
        if position < 0:
            raise ValueError("position cannot be negative")

        if position >= self._len:
            self.append(val)
            self._len += 1
            return

        if position == 0:
            self.prepend(val)
            self._len += 1
            return

        before = self._traverseToPosition(position - 1)
        new_node = Node(val, before.next, before)
        before.next = new_node
        new_node.next.prev = new_node
        self._len += 1

    def remove(self, position: int):
        if position < 0 or position > self._len:
            raise ValueError(f"position {position} out of range")

        before = self._traverseToPosition(position - 1)
        before.next = before.next.next
        self._len -= 1

    def __str__(self):
        values = []
        curr = self.head
        while curr != None:
            values.append(curr.value)
            curr = curr.next
        return str(values)

    def reverse(self):
        if not self.head.next:
            return

        first = self.head
        self.tail = self.head
        second = first.next

        while second:
            tmp = second.next
            second.next = first
            first = second
            second = tmp

        self.head.next = None
        self.head = first
