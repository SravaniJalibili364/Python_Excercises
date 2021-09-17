'''Prompt user to enter a sequence of comma-separated numbers and generate a list and a tuple with those numbers'''


# Taking input as sequence of numbers with comma-separated using split function
Numbers_list = list(map(int,input().split(",")))      
                                                      

# Now tuple will print with numbers as an list items
print("List:",Numbers_list)                             

Tuple_List = tuple(Numbers_list)  
# Now tuple will print with numbers as an tuple items
print("Tuple",Tuple_List)                               