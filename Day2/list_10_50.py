
'''For a given list, generate a list containing squares of the items in list that are greater than 10 and less than 50.'''

def square_num_condition(input_list):
    square_list = []
    for i in input_list:
        if (i > 10 and i < 50):
            square_list.append(i**2)
    return square_list

input_list = list(map(int,input().split()))
result = square_num_condition(input_list)
print(result)
