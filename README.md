# List API

## Overview
This Python program offers a versatile List API capable of performing various operations on lists. It provides functions for manipulating lists, including swapping elements, shifting elements, doubling values, checking sort order, and replacing even numbers.

### Author
- **Author:** Kirti Subramanian
- **CWID:** 20531478
- **Date:** 11/4/2022

## Description
The program includes five primary operations that can be performed on input lists:
1. **Swapping the First and Last Elements**: `swap_first_and_last(input_list)`
2. **Shifting Elements Right and Bringing Last to Front**: `shift_right(input_list)`
3. **Doubling All Elements in the List**: `double(input_list)`
4. **Checking if the List is Sorted**: `is_sorted(input_list)`
5. **Replacing All Even Elements with Zero**: `replace_evens(input_list)`

Each function takes a list as an input and performs the specified operation, with some functions modifying the list in-place.

## Usage
### Example Usage of Functions
```python
# Example for swap_first_and_last function
my_list = [1, 4, 2, 9]
swap_first_and_last(my_list)
print(my_list)  # Outputs: [9, 4, 2, 1]

# Example for shift_right function
shift_right(my_list)
print(my_list)  # Outputs: [9, 1, 4, 2]

# Example for double function
double(my_list)
print(my_list)  # Outputs: [2, 8, 4, 18]

# Example for is_sorted function
print(is_sorted(my_list))  # Outputs: False
print(is_sorted([1, 2, 4, 9]))  # Outputs: True

# Example for replace_evens function
replace_evens(my_list)
print(my_list)  # Outputs: [1, 0, 0, 9]
