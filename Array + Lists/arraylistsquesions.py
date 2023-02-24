import numpy as np

# Question 1 - How to find the missing integer in an array of 1 to 100?

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
length_list = len(my_list)
print(length_list)

def find_missing(custom_list, n):
    # We can find the missing number using the equation (n+1)*(n+2)/2
    # Where N is the number of elements in the list
    sum1 = (n + 1) * (n + 2) / 2
    sum2 = sum(custom_list)
    # We then add up all numbers in the list, subtract the sums from each other, and receive the missing integer
    print(sum1 - sum2)

# find_missing(my_list, length_list)


# Question 2 - Find two numbers in an array whose sum is equal to the target number

list_pairs = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def find_pairs(custom_array, target_sum):
    # We start by iterating over the list / array, with the first index in the first for loop, and the index right after
    # It in the second for loop. With this loop we are ignoring integers that are the same and only returning
    # Unique pairs that equal our target sum
    for i in range(len(custom_array)):
        for j in range(i + 1, len(custom_array)):
            if custom_array[i] == custom_array[j]:
                continue
            if custom_array[i] + custom_array[j] == target_sum:
                print(i, j)

# find_pairs(list_pairs, 6)


# Question 3 - How to test if an array / list contains a number in Python
my_array_q_3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

def find_number(custom_array, target_number):
    # This is simply done by iterating over the loop and checking each value to see if they match our target number
    for i in range(len(custom_array)):
        if custom_array[i] == target_number:
            print(custom_array[i])
        else:
            print('The number does not exist')
# find_number(my_array_q_3, 17)

# Question 4 - How to find maximum product of two integers in the array where all elements are positive
my_array_q_4 = np.array([1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 35, 16, 27, 58, 19, 21])

def find_maximum_product(custom_array):
    # In order to find the two integers that give us the largest product when multiplied we start by defining a variable
    # with a value equal to 0, and then similarly to the Finding Pairs function we iterate over each number, starting
    # With the first and second index, and iterate over each value thereafter, updating the variable we initally set
    # When the product of those two numbers is greater than the current value.
    max_product = 0
    for i in range(len(custom_array)):
        for j in range(i + 1, len(custom_array)):
            if custom_array[i] * custom_array[j] > max_product:
                max_product = custom_array[i] * custom_array[j]
                pairs = str(custom_array[i]) + "," + str(custom_array[j])
    print(pairs)
    print(max_product)

find_maximum_product(my_array_q_4)

# Question 5 - Create an algorithm to check that all elements in a list are unique
my_list_q_5 = [1, 51, 72, 124, 71, 15, 62, 111, 552, 1]

def check_for_unique(custom_list):
    # Checking a list to make sure all elements inside are unique, first we create an empty list, and then for each
    # Element inside the list we first check to see if the element is inside our new list created by calling the function
    # And if its not, we append it in, and if it is, we return false as all elements in the list are not unique.
    checked_elements = []
    for i in custom_list:
        if i in checked_elements:
            print(i)
            return False
        else:
            checked_elements.append(i)
    return True

# print(check_for_unique(my_list_q_5))

# Question 6 - Given two strings, check if one is a permutation ( same characters, different orders) of another

my_list_q_6a = [1, 2, 3]
my_list_q_6b = [3, 2, 1]

def check_permutation(custom_list_1, custom_list_2):
    # To check for permutation, we simply sort the list by using the sort keyword, returning the list in ascending order
    # By numerical values, and then compare our lists to see if they hold the same elements, returning True if so
    # And False if not
    if len(custom_list_1) != len(custom_list_2):
        return False
    else:
        custom_list_1.sort()
        custom_list_2.sort()
        if custom_list_1 == custom_list_2:
            return True
        else:
            return False

print(check_permutation(my_list_q_6a, my_list_q_6b))


# Question 7 - Given an image represented by an NxN matrix write a method to rotate the image by 90 degrees
question_7_array = np.array([[1, 2, 3],
                             [4, 5, 6],
                             [7, 8, 9]])

def rotate_matrix(custom_matrix):
    length_of_matrix = len(custom_matrix)
    for layer in range(length_of_matrix//2):
        first = layer
        last = length_of_matrix - layer - 1
        for i in range(first, last):
            # Save the top element
            top = custom_matrix[layer][i]
            # Move left element to top
            custom_matrix[layer][i] = custom_matrix[-i-1][layer]
            # Move bottom element to left
            custom_matrix[-i-1][layer] = custom_matrix[-layer-1][-i-1]
            # Move right element to the bottom
            custom_matrix[-layer-1][-i-1] = custom_matrix[i][-layer-1]
            # Move top to right
            custom_matrix[i][-layer - 1] = top

    return custom_matrix

print(rotate_matrix(question_7_array))

# Question 8 - Write a function that takes a list and returns all elements except for the first and last elements
question_8_list = [1, 2, 3, 4, 5]

def find_middle(custom_list):
    middle_elements = custom_list[1:-1]
    return middle_elements

# The answer the course gave was
def middle(custom_list):
    new = custom_list[1:]
    del new[-1]
    return new

print(find_middle(question_8_list))

# Question 9 - Given a 2D list, calculate the sum of diagonal elements
myList2D= [[1,2,3],[4,5,6],[7,8,9]]
def sum_of_diagonal(custom_list):
    index = 0
    new_list = []
    for i in custom_list:
        new_list.append(i[index])
        index +=1
    product = np.product(new_list)
    print(product)

sum_of_diagonal(myList2D)

# The answer the course gave was, and I misread and did product and not sum lol
def sum_diagonal(a):
    sum_of_list = 0
    for i in range(len(a)):
        sum_of_list += a[i][i]
    return sum_of_list

# Question 10 - Given a list, write a function to find the first and second best scores

scores_list = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]

def find_best(custom_list):
     custom_list.sort(reverse=True)
     return custom_list[:2:]

print(find_best(scores_list))

# The answer the course gave is
def firstSecond(given_list):
    a = given_list  # make a copy
    a.sort(reverse=True)
    print(a)
    first = a[0]
    for element in given_list:
        if element != first:
            second = element
            return first, second

# Where you make a copy of the list, sort it, and take the first element from said list. Then you iterate through
# The list and compare each element to the first one you took, that way it excludes any duplicates, and then returns
# The two elements taken from the list

# Question 11 - Find the Missing sum, which we'd already done, yet when i plug in the algorithm or equation
# He told us, it doesn't work in this setting
def missingNumber(myList, totalCount):
    expectedSum = totalCount * ((totalCount + 1) / 2)
    actualSum = 0
    for i in myList:
        actualSum += i
    return int(expectedSum - actualSum)

# So you take the total count, do the n * n+1 / 2, you then get the sum of the list by adding it all together,
# and then subtract those two. A different way of doing it, but I understand it.

duplicated_list = [1, 1, 2, 2, 3, 4, 5]

def removeDuplicates(myList):
    new_list = []
    for i in myList:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(removeDuplicates(duplicated_list))