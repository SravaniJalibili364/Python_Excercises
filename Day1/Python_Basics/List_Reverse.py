'''Question - Prompt user for first, last names and print them in reverse order.'''


# Defining the function to reverse the string
def reverse_strng_function(full_name):
    # creating the empty variable for to store the string                     
    reverse_string = ""  
    # Iterating the string usinf for loop                                  
    for i in full_name:
         # it will add every letter to the beginning of the string                                    
        reverse_string = i + reverse_string               

    #It will return the reversed string 
    return reverse_string

#Taking first_name as input from the user
f_name = input()
 #Taking second_name as input from the user                                        
l_name = input()                                      
Full_name = f_name+ l_name
#result = Full_name[::-1] - this is the builtin method to print the reverse of the string

#Calling function to reverse the string and it will return to output_rev_string variable                                 
output_rev_string = reverse_strng_function(Full_name)       
 # It will print the reverse of the string
print(output_rev_string)                                   

