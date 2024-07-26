def bubble_sort():  # create a function for bubble sort
    list_nums = nums[:]  # create a copy of the original array
    # sorting direction depending on parity. If the number is even - ascending, otherwise - descending.
    swap_bool = True  # set the True flag so that the sorting is not infinite
    if parity:  # if the number is even, sort in ascending order
        while swap_bool:  # we start the while loop
            swap_bool = False  # change the flag to False
            for i in range(len(list_nums) - 1):  # we start the for loop
                if list_nums[i] > list_nums[i + 1]:  # compare the first 2 elements.
                    # If 1st > next, swap
                    list_nums[i], list_nums[i + 1] = list_nums[i + 1], list_nums[i]
                    swap_bool = True  # change the flag to True again
    else:  # if the number is odd, sort in descending order
        while swap_bool:
            swap_bool = False
            for i in range(len(list_nums) - 1):  # we start the for loop
                if list_nums[i] < list_nums[i + 1]:  # compare the first 2 elements.
                    # If 1st < next, swap
                    list_nums[i], list_nums[i + 1] = list_nums[i + 1], list_nums[i]
                    swap_bool = True  # change the flag to True again
    return list_nums  # return value - sorted list


def insertion_sort():  # create a function for insertion sort
    list_nums = nums[:]  # create a copy of the original array
    # sorting direction depending on parity. If the number is even - ascending, otherwise - descending.
    if parity:  # if the number is even, sort in ascending order
        for i in range(1, len(list_nums)):  # We start the sorting cycle from the 2nd element (with index 1),
            # 1 element (with index 0) is considered sorted
            temp = list_nums[i]  # We save the sorted element in a variable
            j = i - 1  # Sorted elements are moved to the beginning if they are > the element to insert
            while j >= 0 and list_nums[j] > temp:  # loop while sorted element is non-negative and > temp
                list_nums[j + 1] = list_nums[j]  # swap the insert element and the sorted element
                j -= 1  # Insert element
            list_nums[j + 1] = temp  # After the end of the cycle, save the next insert element into the temp variable
    else:  # if the number is odd, sort in descending order
        for i in range(1, len(list_nums)):  # We start the sorting cycle from the 2nd element (with index 1),
            # 1 element (with index 0) is considered sorted
            temp = list_nums[i]  # We save the sorted element in a variable
            j = i - 1
            while j >= 0 and list_nums[j] < temp:  # loop while sorted element is non-negative and < temp
                list_nums[j + 1] = list_nums[j]  # swap the insert element and the sorted element
                j -= 1  # Insert element
            list_nums[j + 1] = temp  # After the end of the loop, we save the next sorting element in the temp variable.
    return list_nums  # return sorted list


def count_mean_square():  # function to find the mean square of a set of data
    sum_squares = sum([i * i for i in nums])  # the sum of the numbers in a list in which all elements are first squared
    average_sum = sum_squares / len(nums)  # we find the average value of the sum by dividing
    # sum of list values by number of elements
    return round(average_sum ** 0.5, 3)  # the return value is the root mean of the sum,
    # rounded to 3 decimal places


def count_arithmetic_mean():  # function for finding the arithmetic mean of a set of numbers
    total = sum(nums)  # find the sum of all numbers in the list
    return round(total / len(nums), 3)  # return value rounded to 3 decimal places ratio
    # the sum of the numbers in a list by the number of numbers in the list (or the length of the list)


# reading file in default mode - reading mode; Unicode encoding - utf-8
with open("source_data.txt", encoding='utf-8') as file:
    surname_name_patronymic = file.readline()[:-1]  # save in variable full name
    student_id = file.readline()  # save in variable ID

# we will form a list of unicode codes from each character of the full name, translated into decimal form - ascii
nums = [ord(character) for character in surname_name_patronymic.replace(' ', '')]  # replace method to replace spaces
# the number resulting from dividing the ID by the number of characters that make up the full name
number = int(int(student_id) / len(nums))
# determine the parity of a number if the remainder when divided by 2 is zero-the number is even
parity = number % 2 == 0
increasing_decreasing = 'ascending' if parity else 'descending'  # determine increase/decrease
sort_nums_1 = bubble_sort()  # save bubble sort call to variable
sort_nums_2 = insertion_sort()  # save insertion sort call to variable

arithmetic_mean = count_arithmetic_mean()  # call a function to find the arithmetic mean
mean_square = count_mean_square()  # call function to find mean square

# formation of the result
result = f"""1. Source data: {surname_name_patronymic}; ID: {student_id}
2. {number}
3. Sorting direction: by {increasing_decreasing}, since the number {number} – {'even' if parity else 'odd'} 
4. Data set: {nums}
5. Sorted by {increasing_decreasing} dataset {sort_nums_1}
7. Arithmetic mean: {arithmetic_mean}
8. Mean Square value: {mean_square}
"""
# If you need to sort using the 2nd method - insertions: above in point 5. replace sort_nums_1 with sort_nums_2

# write result to file
with open("result.txt", "w", encoding='utf-8') as file:
    file.write(result)  # Using the file's write() method, we write the result string to the file.
