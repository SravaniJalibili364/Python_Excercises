'''Question - Split the following string into a list using the separator and print the first, last elements'''



# Taking the input as string with hypen separated and using split function it converting into list
str_input = input().split("-") 
# It will print the firstelement and lastelement of the list                       
print(str_input[0],str_input[-1])                     