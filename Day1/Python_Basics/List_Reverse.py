#Prompt user for first, last names and print them in reverse order.


def reverse_strng_function(full_name):
    reverse_string = ""
    for i in Full_name:
        reverse_string = i + reverse_string

    return reverse_string

first_name = input()
second_name = input()
Full_name = first_name + second_name
#result = Full_name[::-1]      #this is the builtin function
output_rev_string = reverse_strng_function(Full_name)
print(output_rev_string)

