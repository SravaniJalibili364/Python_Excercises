#For a given list, generate a list containing squares of the items in list that are greater than 10 and less than 50.
def result(lst):                        #declaring a function taking lsit as argument
    empty_list=[]                       #declaring empty list
    for ele in lst:                     #iterating each ele in the list
        if ele>10 and ele<50:           #checking the list ele is greater than 10 and less than 50 
            empty_list.append(ele**2)   #squaring the ele
    print(empty_list)                   #printing the list

list_=map(int,input().split(","))
result(list_)
#Here i have taken list from user.And then i have called result function.In result function passed a list as a argument.Declare a one empty list.After that by using for loop iterate each ele and check if the element is greater than 10 and less ahn 50.If it is satisfies that condition then square that element add to empty list.Finally print that list.