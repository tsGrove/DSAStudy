# Question 1 : Describe how you could use a single Python list to implement three stacks
# Fixed division approach

class MultiStack:
    def __init__(self, stack_size):
        self.number_of_stacks = 3
        self.custom_list = [0] * (stack_size * self.number_of_stacks)
        self.sizes = [0] * self.number_of_stacks
        self.stack_size = stack_size


    def is_full(self, stack_number):
        if self.sizes[stack_number] == self.stack_size:
            return True
        else:
            return False

    def is_empty(self, stack_number):
        if self.sizes[stack_number] == 0:
            return True
        else:
            return False

    def top_index(self, stack_number):
        offset = stack_number * self.stack_size
        return offset + self.sizes[stack_number] - 1


    def push(self, value, stack_number):
        if self.is_full(stack_number):
            return "The stack is full"
        else:
            self.sizes[stack_number] =+ 1
            self.custom_list[self.top_index(stack_number)] = value


    def pop(self, stack_number):
        if self.is_empty(stack_number):
            return 'The stack is empty'
        else:
            value = self.custom_list[self.top_index(stack_number)]
            self.custom_list[self.top_index(stack_number)] = 0
            self.sizes[stack_number] -= 1
            return value

    def peek(self, stack_number):
        if self.is_empty(stack_number):
            return 'The stack is empty'
        else:
            value = self.custom_list[self.top_index(stack_number)]
            return value


# custom_stack = MultiStack(6)
# print(custom_stack.is_full(0))
# print(custom_stack.is_empty(1))
# custom_stack.push(1, 0)
# custom_stack.push(2, 0)
# custom_stack.push(3, 2)
# print(custom_stack.peek(1))
# print(custom_stack.peek(2))


# Question 2 - Stack Min
# How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element?
# Push, pop, and min should all operate in O(1).

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        string = str(self.value)
        if self.next:
            string += "," + str(self.next)
        return string

class Stack:
    def __init__(self):
        self.top = None
        self.minimum_node = None

    def min(self):
        if not self.minimum_node:
            return None
        else:
            return self.minimum_node

    def minimum_push(self, value):
        if self.minimum_node and (self.minimum_node.value < value):
            self.minimum_node = Node(value= self.minimum_node.value, next_node=self.minimum_node)
        else:
            self.minimum_node = Node(value=value, next_node=self.top)
        self.top = Node(value=value, next_node=self.top)

    def minimum_pop(self):
        if not self.top:
            return None
        self.minimum_node = self.minimum_node.next
        item = self.top.value
        self.top = self.top.next
        return item

# minimum_value_stack = Stack()
# minimum_value_stack.minimum_push(5)
# print(minimum_value_stack.min())


# Question 3 :
# Image a stack of plates, if the stack gets too high, the plates might fall over! Therefore, in real life, we would
# Likely start a new stack when the previous stack exceeds some threshold. Implement a data structure SetOfStacks
# That mimics this. SOS should be composed of several stacks and should create a new stack once the previous one
# Exceeds capacity. SOS.push() and SOS.pop() should behave identically to a single stack (that is, pop() should return
# # The same values as it would if it were just a single stack)

class PlateStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def __str__(self):
        return self.stacks

    def plate_push(self, value):
        if len(self.stacks) > 0 and (len(self.stacks[-1])) < self.capacity:
            self.stacks[-1].append(value)
        else:
            self.stacks.append([value])

    def plate_pop(self):
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1]

    def pop_at(self, stack_number):
        if len(self.stacks[stack_number]) > 0:
            return self.stacks[stack_number].pop()
        else:
            return None

# plate_stacking = PlateStack(2)
# plate_stacking.plate_push(1)
# plate_stacking.plate_push(2)
# plate_stacking.plate_push(3)
# plate_stacking.plate_push(4)
# plate_stacking.plate_push(5)
# print(plate_stacking.plate_pop())
# print(plate_stacking.pop_at(1))


# Question 4 : Implement a Queue class which implements a queue using two stacks

class QueueStack:
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def queue_push(self, value):
        self.list.append(value)

    def queue_pop(self):
        if len(self.list) == 0:
            return None
        return self.list.pop()

class QueueViaStack:
    def __init__(self):
        self.inner_stack = QueueStack()
        self.outer_stack = QueueStack()

    def enqueue(self, item):
        self.inner_stack.queue_push(item)

    def dequeue(self):
        while len(self.inner_stack):
            self.outer_stack.queue_push(self.inner_stack.queue_pop())
        result = self.outer_stack.queue_pop()
        while len(self.outer_stack):
            self.inner_stack.queue_push(self.outer_stack.queue_pop())
        return result
#
# customQueue = QueueViaStack()
# customQueue.enqueue(1)
# customQueue.enqueue(2)
# customQueue.enqueue(3)
# print(customQueue.dequeue())
# customQueue.enqueue(4)
# print(customQueue.dequeue())


# An animal shelter, which only holds dogs and cats, operates on a strictly "FIFO" basis. People must adopt either the
# "oldest" (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or
# a cat, and will receive the oldest animal of that type. They cannot select which specific animal they would like. Create
# the data structures to maintain this system, and implement operations such as enqueue, dequeue, dequeueDog, dequeueCat

class ShelterQueue:
    def __init__(self):
        self.cats = []
        self.dogs = []

    def shelter_enqueue(self, animal, breed):
        if breed.lower() == 'cat':
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def cat_dequeue(self):
        if len(self.cats) == 0:
            return 'No cats :('
        else:
            cat = self.cats.pop(0)
            return cat

    def dog_dequeue(self):
        if len(self.dogs) == 0:
            return 'No dogs :('
        else:
            dog = self.dogs.pop(0)
            return dog

    def dequeue_animal(self):
        if len(self.cats) == 0:
            result = self.dogs.pop(0)
        else:
            result = self.cats.pop(0)
        return result

animal_queue = ShelterQueue()
animal_queue.shelter_enqueue('dog1', 'dog')
animal_queue.shelter_enqueue('cat1', 'cat')
animal_queue.shelter_enqueue('dog2', 'dog')
animal_queue.shelter_enqueue('dog3', 'dog')
animal_queue.shelter_enqueue('dog4', 'dog')
animal_queue.shelter_enqueue('cat2', 'cat')
print(animal_queue.cat_dequeue())
