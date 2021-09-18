'''Generate a list containing squares of the numbers 0 - 9.'''


# defining the function for the square of the number
def square(n):
    # now square of the number will store in s
    s = n*n
    return s

nn = list(range(1,10))
# Now calling the square function and then mapping square function to every list item
result = list(map(square,nn))
print(result)