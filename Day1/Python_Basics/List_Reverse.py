#Prompt user for first, last names and print them in reverse order.


def reverse_strng_function(full_name):                     # Defining the function to reverse the string
    reverse_string = ""                                    # creating the empty variable for to store the string
    for i in Full_name:                                    # Iterating the string 
        reverse_string = i + reverse_string                # it will every letter to the first

    return reverse_string

f_name = input()                                        #Taking first_name as input from the user
l_name = input()                                       #Taking second_name as input from the user
Full_name = f_name+ l_name
#result = Full_name[::-1]                                   # this is the builtin method to print the reverse of the string
output_rev_string = reverse_strng_function(Full_name)       # Calling function to reverse the string and it will return to output_rev_string variable
print(output_rev_string)                                    # It will print the reverse of the string

