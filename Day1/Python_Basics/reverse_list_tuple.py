'''Prompt user for first, last names and print them in reverse order.'''


def reverse_string(Full_name):                 # Now reverse_string function is for converting list to string
    full_name_reverse = ""                     # Now empty variable taking for storing the variable
    for letter in Full_name:                   # using for loop we are using iterating through the list
        full_name_reverse += letter            # Now we are using adding every char to that string

    return full_name_reverse                    # Now we are returning the string



first_name = list(input())                       # Taking first name as input from the user as a string and it converts to list
second_name = tuple(input())                     # Taking second name as input from the user and it converst to tuple

Full_name = first_name + list(second_name)       # firstname and lastname will concatenate to fullname
result = Full_name[::-1]                         # Now the entire list will store in reverse order

reverse_full_name = reverse_string(result)       # now reverse_string function calling
print(reverse_full_name)                         # fullname will print in reverse order


