
'''Write a Python program that verifies if a number is within variance of the range limits.
'''

# Defining the function to calculate the variance of the two numbers
def variance_of_the_number(f_number,s_number):
    Diff_between_number = abs(f_number - s_number)
    division_ = Diff_between_number / f_number
    Variance_ = abs(division_*100)
    return int(Variance_)

f_number = int(input("Lower Limit"))
s_number = int(input("Upper Limit"))
n = int(input("Number"))
result = variance_of_the_number(f_number,s_number)
# Now Checking whether the number is within range or not
if n < result:
    print("Number is within variance of range limits")
else:
    print("It was not in the variance of the range limits")
