'''Prompt user for first, last names and print them in reverse order.'''


# Now reverse_string function is for converting list to string
def reverse_string(Full_name):                 
    full_name_reverse = ""                     
    for letter in Full_name:                   
        full_name_reverse += letter            

    return full_name_reverse                    


# Taking first name as input from the user as a string and it converts to list
first_name = list(input())     
# Taking second name as input from the user and it converst to tuple                  
second_name = tuple(input())                     

# Now the entire list will store in reverse order
Full_name = first_name + list(second_name)       
result = Full_name[::-1]                         

# now reverse_string function calling
reverse_full_name = reverse_string(result)       
print(reverse_full_name)                        


