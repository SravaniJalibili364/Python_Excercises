'''Print the identity of an object.'''

#taking the input from user as character 
char = input()
# using the id() inbuilt function we can return the identity of an object
Id_char = id(char)
# It prints id of the object
print(Id_char)