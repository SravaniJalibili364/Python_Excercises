'''Prepare a list of tuples by pairing each element from second list with element from first list'''
def mapping_list(first_list,second_list):
    len_first_list  = len(first_list)
    len_second_list = len(second_list)
    if(len_first_list == len_second_list):
        pairing_list = []
        for i in range(len_second_list):
             tuple_as_item = []
             tuple_as_item += [first_list[i],second_list[i]]
             tuple_as_item = tuple(tuple_as_item)
             pairing_list.append(tuple_as_item)
        print(pairing_list)
    else:
       print("Length of two lists are not equal")



list_1=list(map(int,input().split()))
list_2=list(map(int,input().split()))
result = mapping_list(list_1,list_2)