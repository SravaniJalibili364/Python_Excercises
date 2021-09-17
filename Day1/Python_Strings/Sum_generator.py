''''Create a function digit_range_sum_gnrt that accepts two values (d, n) and does the following '''


#Defining the function for the operation
def digit_range_sum_gnrt(d,n):
    #taking an empty variable to store the sum of the list items
    Total_sum = 0
    #Declaring an empty list for storing the variables
    List_Num = []
    #Using the for loop it takes the numbers from 1 to n+1
    for i in range(1,n+1):
        # It is storing the number into i times
        num_recc = int(i*str(d))
        #now that number is appended to the list 
        List_Num.append(num_recc)
        # it will store entire sum into total 
        Total_sum += num_recc
    
    #It will return the list and sum
    return List_Num,Total_sum


#taking the input from the user which number has to recurrence
a = int(input())
#taking the input for how many times the number has to recurrence
b = int(input())
# Calling the function to return the list and sum of the list
list,output = digit_range_sum_gnrt(a,b)
#Now the list and total sum will print
print(list)
print(output)