from random import randint

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)
class LinkedList:
    def __init__(self, values = None):
        self.head = None
        self.tail = None

    def __iter__(self):
        # Created in order to make the Linked List iterable
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next

    def __str__(self):
        # Created so that the Linked List is printable
        values = [str(x.value) for x in self]
        return "->".join(values)

    def __len__(self):
        # Created so you may know the length of any given Linked List
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def add(self, value):
        # Function which adds a node to a linked list by first checking if it is empty, and then adding it to the end
        # Otherwise
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def generate_linked_list(self, n, minimum_value, maximum_value):
        # Generates a random linked list based on n, or number of nodes, and a minimum and maximum value
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(minimum_value, maximum_value))
        return self
