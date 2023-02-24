from LinkedListClass import LinkedList, Node

# Question 1 - Remove duplicates from an unsorted linked list

sample_linked_list = LinkedList()
print(sample_linked_list.generate_linked_list(10, 0, 99))

def remove_duplicates(custom_list):
    # First checks to see that the Linked List is populated by Nodes, otherwise function ends
    if custom_list.head is None:
        return
    else:
        # If nodes exist, we start by iterating over the list with the head value, and add it to the set.
        current_node = custom_list.head
        visited = { current_node.value }
        # And while there is a next node to iterate over, if the value of next node is already in our set, we skip over it
        # Otherwise we add it to our set, and keep iterating, and at the end of it all return our new linked list with no
        # Duplicates
        while current_node.next:
            if current_node.next.value in visited:
                current_node.next = current_node.next.next
            else:
                visited.add(current_node.next.value)
                current_node = current_node.next
        return custom_list
        # TC : O(n), SC: O(1)

# custom_linked_list = LinkedList()
# custom_linked_list.generate_linked_list(10, 0, 10)
# print(custom_linked_list)
# print(remove_duplicates(custom_linked_list))

# Question 2 - Implement an algorithm to find the nth to last element of a single linked list, assuming we dont know the
# Length of the linked list

def nth_to_last(custom_linked_list, n):
    # First we create two pointers, which are n nodes apart
    pointer_1 = custom_linked_list.head
    pointer_2 = custom_linked_list.head
    for i in range(n):
        if pointer_2 is None:
            return None
        pointer_2 = pointer_2.next
    # Next we will move through the list, until pointer 2 reaches the last node, and due to them being n nodes apart
    # We know that pointer 1 will have stopped at the position we are looking for
    while pointer_2:
        pointer_1 = pointer_1.next
        pointer_2 = pointer_2.next
    return pointer_1
    # TC : O(n), SC: O(1)
# print(nth_to_last(sample_linked_list, 3))

# Question 3 - Write code to partition a linked list around a value x, such that all nodes less than x come before all
# nodes greater to or equal to x

def partition(custom_linked_list, x):
    # We begin by creating a node at the head of the Linked list, and making the tail point to the head
    current_node = custom_linked_list.head
    custom_linked_list.tail = custom_linked_list.head

    # We then begin to iterate over each node, checking their values, if the value is less than x, we place it to the
    # left, and if it greater, we place it at the end of the linked list, or make it the tail
    while current_node:
        next_node = current_node.next
        current_node.next = None
        if current_node.value < x:
            current_node.next = custom_linked_list.head
            custom_linked_list.head = current_node
        else:
            custom_linked_list.tail.next = current_node
            custom_linked_list.tail = current_node
        current_node = next_node

    if custom_linked_list.tail.next is not None:
        custom_linked_list.tail.next = None
    # TC: O(n), SC: O(1)

# partition(sample_linked_list, 50)
# print(sample_linked_list)

# Question 4 - You have two numbers represented by a linked list, where each node contains a single digit.
# The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function
# That adds the two numbers and returns the sum of the linked list

def sum_of_two_lists(custom_linked_list_a, custom_linked_list_b):
    # We start by craeting 2 temporary nodes, one for each head of the linked lists we are adding together,
    # And creating an empty linked list to store our results
    temp_node_1 = custom_linked_list_a.head
    temp_node_2 = custom_linked_list_b.head
    carry = 0
    sum_of_lists = LinkedList()

    # Next we go through and add each integer from each list one at a time, taking anything over 10 and adding that
    # Extra digit to the next round of additions we make, and once that is done we return the new linked list
    while temp_node_1 or temp_node_2:
        result = carry
        if temp_node_1:
            result += temp_node_1.value
            temp_node_1 = temp_node_1.next

        if temp_node_2:
            result += temp_node_2.value
            temp_node_2 = temp_node_2.next

        sum_of_lists.add(int(result % 10))
        carry = result / 10

    return sum_of_lists
    # TC + SC O(n)
# linked_list_a = LinkedList()
# linked_list_b = LinkedList()
#
# linked_list_a.add(7)
# linked_list_a.add(1)
# linked_list_a.add(6)
#
# linked_list_b.add(5)
# linked_list_b.add(9)
# linked_list_b.add(2)
#
# print(linked_list_a, linked_list_b)
# print(sum_of_two_lists(linked_list_a, linked_list_b))

# Question 5 - Given two single linked lists, determine if the two lists intersect. Return the intersecting node.
# Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked list
# Is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.

def intersecting_linked_lists(custom_linked_list_a, custom_linked_list_b):
    if custom_linked_list_a.tail is not custom_linked_list_b.tail:
        return False

    length_a = len(custom_linked_list_a)
    length_b = len(custom_linked_list_b)

    shorter_list = custom_linked_list_a if length_a < length_b else custom_linked_list_b
    longer_list = custom_linked_list_b if length_a > length_b else custom_linked_list_a

    difference = len(longer_list) - len(shorter_list)

    longer_node = longer_list.head
    shorter_node = shorter_list.head

    for i in range(difference):
        longer_node = longer_node.next

    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    return longer_node

def add_same_node(linked_list_a, linked_list_b, value):
    temp_node = Node(value)

    linked_list_a.tail.next = temp_node
    linked_list_a.tail = temp_node

    linked_list_b.tail.next = temp_node
    linked_list_b.tail = temp_node

