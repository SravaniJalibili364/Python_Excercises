'''Prompt user to enter a number and print out the digits missing from the number'''

# defining the function to findout the missing numbers
def missing_num(input_list,sorted_list):
    set_ = set()
    for i in input_list:
        if i not in sorted_list:
            set_.add(i)

    print(set_)

n = list(map(int,input().split()))
sorted_list = sorted(n)
input_list = range(1,10)
missing_num(input_list,sorted_list)
        
