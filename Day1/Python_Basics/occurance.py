'''count the number occurrence of a specific character in a string.'''

# Taking string as input from the user
String_ = input()  
# Taking char as input from the user         
char    = input() 
# assaigning '0' to the "c" variable          
c       = 0 
# Iterating string using for loop                
for i in String_: 
# Checking the condition if given char is equal to the char of the string           
    if(char == i):         
        # Then count will increment to 1         
        c += 1                  

#It will print the occurance of the character
print(c)                  
