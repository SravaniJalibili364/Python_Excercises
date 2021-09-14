def result(l1,l2):
    len1=len(l1)
    len2=len(l2)
    temp=[]
    if len1==len2:
        for i in range(len1):
             temp2=[]
             temp2=temp2+[l1[i],l2[i]]
             temp2 = tuple(temp2)
             temp=temp+[temp2]
        print(temp)
    else:
       print("Length of two lists are not equal")



list_1=list(map(int,input().split(",")))
list_2=list(map(int,input().split(",")))
result(list_1,list_2)
