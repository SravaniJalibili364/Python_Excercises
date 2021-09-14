def even_items_in_Given_list(lst):     #function declaraion
    even_list=[]                       #declare empty list
    for ele in lst:                    #iterating each ele in the list
        if ele%2==0:                   #checking the ele is even or not
            even_list.append(ele)      #appending even ele to the even_list
    print(even_list)                   #printing even num list

lst_=[1,2,3,4,5,6,8,67,90,34,866,8900]      #given list
even_items_in_Given_list(lst_)              #function calling

#First take input list and then create a function that prints the even elements in the given list.In the function pass list as argument.Declare a empty list.By using for loop iterate each ele and check if it is even or not.If it is even then add that element to the even_empty list and finally print that list outside of th for loop