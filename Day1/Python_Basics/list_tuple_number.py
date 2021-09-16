#Prompt user to enter a sequence of comma-separated numbers and generate a list and a tuple with those numbers

Num_input = input()                                     # Taking input as sequence of numbers with comma-separated
Numbers_list = list(map(int,Num_input.split(",")))      # Using split function sequence of numbers converted into list and then each number
                                                        # converted into int type from string type

print("List:",Numbers_list)                             # Now it will print the numbers list
Tuple_List = tuple(Numbers_list)                        # List converting into tuple 

print("Tuple",Tuple_List)                               # Now tuple will print with numbers as an tuple items