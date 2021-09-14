n = list(map(int,input()))
sorted_list = sorted(n)
set_ = set()
input_list = [0,1,2,3,4,5,6,7,8,9]
for i in input_list:
    if i not in sorted_list:
        set_.add(i)

    
print(set_)
        
