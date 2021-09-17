'''Prompt user to enter a number and then print out message if it is odd or even.'''


#defining the function whether the number is even or odd
def even_odd(n):
    if(n % 2 == 0):
        print("Even")
    else:
        print("Odd")

n = int(input())
even_odd(n)