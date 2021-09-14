#Generate a list containing squares of the numbers 0 - 9.
def list_squares(li):                   # defining the list_squares function for the numbers squares
    sq_list = []                        # Taking an empty to store the squres of the list
    for num in li:                      # Iterating the list using the for loop
        square_num = num**2             # using ** we can get the square of the number
        sq_list += [square_num]         # all the squres will be added to the empty list

    return sq_list                      # It will return squres list


l = list(range(0,10))                    # Taking the integers from 1 to 9 using range function
result = list_squares(l)                 # calling list_squares function and it will return the list containing squares of the numbers
print(result)                            # it will print the list containing the squeares of the numbers in the list



# By using functions we can easily get the expected output 
# list iterating the numbers (0-9) and using the we can get the square of the number using power(**)and then function will return the squres of the list items.