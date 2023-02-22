import numpy as np

# Question 1 - How to find the missing integer in an array of 1 to 100?

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
length_list = len(my_list)
print(length_list)

def find_missing(custom_list, n):
    sum1 = (n + 1) * (n + 2) / 2
    sum2 = sum(custom_list)
    print(sum1 - sum2)

# find_missing(my_list, length_list)


# Question 2 - Find two numbers in an array whose sum is equal to the target number

list_pairs = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def find_pairs(custom_array, target_sum):
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
    for i in range(len(custom_array)):
        if custom_array[i] == target_number:
            print(custom_array[i])
        else:
            print('The number does not exist')
# find_number(my_array_q_3, 17)

# Question 4 - How to find maximum product of two integers in the array where all elements are positive
my_array_q_4 = np.array([1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 35, 16, 27, 58, 19, 21])

def find_maximum_product(custom_array):
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
