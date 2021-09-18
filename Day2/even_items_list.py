
'''For a given list, generate a list containing even items in list.'''
             


def square(n):
    if(n%2 == 0):
        return n


list_input = list(map(int,input().split()))
# Filter fumction will filter the values in the list if the number is even
result = filter(square,list_input)
print(list(result))

