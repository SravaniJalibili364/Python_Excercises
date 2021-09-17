''''Create a function digit_range_sum_gnrt that accepts two values (d, n) and does the following '''


#Defining the function for the operation
def digit_range_sum_gnrt(d,n):
    Total_sum = 0
    List_Num = []
    #Using the for loop it takes the numbers from 1 to n+1
    for i in range(1,n+1):
        # It is storing the number into i times
        num_recc = int(i*str(d))
        List_Num.append(num_recc)
        Total_sum += num_recc
    
    return List_Num,Total_sum


a = int(input())
b = int(input())
# Calling the function to return the list and sum of the list
list,output = digit_range_sum_gnrt(a,b)
#Now the list and total sum will print
print(list)
print(output)