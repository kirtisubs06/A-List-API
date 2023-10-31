"""
Assignment 6: "A List API"

Author: Kirti Subramanian
CWID: 20531478
Date: 11/4/2022

Program Description: This program takes in an input list and can perform 5 different operations
on the list depending on the function called. The possible operation include the following:
1) swapping the first and last elements of the list
2) bringing the last element of the list to the front of the list and shifting the remaining elements to the right
3) doubling all the elements in the list
4) checking whether the list is sorted or not
5) replacing all the even elements in the list with 0
"""


def swap_first_and_last(input_list):
    """
    Modifies the input list by swapping its first and last elements.
    :param input_list: input list
    :return: none
    """
    a = input_list[0]
    input_list[0] = input_list[len(input_list) - 1]
    input_list[len(input_list) - 1] = a


def shift_right(input_list):
    """
    Modifies the input list by shifting all elements in the list to the right and
    brings the last element to the front of the list.
    :param input_list: input list
    :return: none
    """
    a = input_list[len(input_list) - 1]
    input_list.remove(input_list[len(input_list) - 1])
    input_list.insert(0, a)


def double(input_list):
    """
    Modifies the input list by doubling the value of each element in the list.
    :param input_list: input list
    :return: none
    """
    for i in range(len(input_list)):
        input_list[i] = input_list[i] * 2


def is_sorted(input_list):
    """
    Checks if the input list of integers is sorted or not.
    :param input_list: input list
    :return: True if the list is sorted or False if the list is not sorted
    """
    ascending = True
    i = 1
    while i < len(input_list):
        if input_list[i] < input_list[i - 1]:
            ascending = False
        i += 1
    return ascending


def replace_evens(input_list):
    """
    Replaces any even elements of the input list with a zero.
    :param input_list: input list
    :return: none
    """
    for i in range(len(input_list)):
        if input_list[i] % 2 == 0:
            input_list[i] = 0


# main function that tests all the functions
def main():
    # tests swap_first_and_last()
    print("RUN for: swap_first_and_last(my_list):")
    my_list = [1, 4, 2, 9]
    print(my_list)
    swap_first_and_last(my_list)
    print(my_list)
    print()

    # tests shift_right()
    print("RUN for: shift_right(my_list):")
    my_list = [1, 4, 2, 9]
    print(my_list)
    shift_right(my_list)
    print(my_list)
    print()

    # tests double()
    print("RUN for: double(my_list):")
    my_list = [1, 4, 2, 9]
    print(my_list)
    double(my_list)
    print(my_list)
    print()

    # tests is_sorted()
    print("RUN for: is_sorted(my_list):")
    my_list = [1, 4, 2, 9]
    if is_sorted(my_list):
        print("my_list is sorted")
    else:
        print("my_list is not sorted")
    print()

    print("RUN for: is_sorted(my_other_list):")
    my_other_list = [1, 2, 4, 9]
    if is_sorted(my_other_list):
        print("my_other_list is sorted")
    else:
        print("my_other_list is not sorted")
    print()

    # tests replace_evens()
    print("RUN for: replace_evens(my_list):")
    my_list = [1, 4, 2, 9]
    print(my_list)
    replace_evens(my_list)
    print(my_list)


if __name__ == "__main__":
    main()

# test output
"""
/Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/venv/bin/python /Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/assignment6.py
RUN for: swap_first_and_last(my_list):
[1, 4, 2, 9]
[9, 4, 2, 1]

RUN for: shift_right(my_list):
[1, 4, 2, 9]
[9, 1, 4, 2]

RUN for: double(my_list):
[1, 4, 2, 9]
[2, 8, 4, 18]

RUN for: is_sorted(my_list):
my_list is not sorted

RUN for: is_sorted(my_other_list):
my_other_list is sorted

RUN for: replace_evens(my_list):
[1, 4, 2, 9]
[1, 0, 0, 9]

Process finished with exit code 0
"""