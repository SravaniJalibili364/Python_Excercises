def digit_range_sum_gnrt(a,b):
    Sum = 0
    List_Num = []
    for i in range(1,b+1):
        recc = int(i*str(a))
        List_Num = List_Num + [recc]
        Sum += recc
    
    print(List_Num)
    print(Sum)



a = int(input())
b = int(input())
digit_range_sum_gnrt(a,b)