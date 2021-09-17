'''count the number occurrence of a specific character in a string.'''

String_ = input()  
char    = input() 
c       = 0 
for i in String_: 
    # Checking the condition if given char is equal to the char of the string           
    if(char == i):         
        # Then count will increment to 1         
        c += 1                  


print(c)                  
