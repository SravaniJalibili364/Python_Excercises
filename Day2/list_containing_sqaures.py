def squares_list(list_):                  #creating function by passing list as a argument
    empty_list=[]                         #Empty list 
    for ele in list_:                     #iterating the loop by each ele in the list
        empty_list.append(ele**2)         #squaring  the ele and appending to the empty list
    print(empty_list)                     #printing empty list with the squared values

list_=list(range(0,10))                #taking input list
squares_list(list_)                    #function calling


#Taking list as input and created a function generating list of squared elements with in the specified range