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
