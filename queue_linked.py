class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class Queue:

    def __init__(self, capacity=0):
        self.cap = capacity
        self.front = None
        self.back = None
        self.num_items = 0

    def is_empty(self):
        return self.num_items == 0

    def is_full(self):
        return self.num_items == self.cap

    def enqueue(self, item):
        if self.is_full():
            raise IndexError
        elif self.is_empty():
            n = Node(item)
            n.next = self.back
            self.front = n
        else:
            n = Node(item)
            n.next = None
            self.back.next = n
        self.back = n
        self.num_items += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError
        else:
            self.num_items -= 1
            temp = self.front
            self.front = self.front.next
            return temp

    def size(self):
        return self.num_items
