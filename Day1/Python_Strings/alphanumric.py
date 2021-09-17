''''Prompt user to enter a value and then print value's content type (alpha, numeric, alphanumeric).
'''


Input= input()
# It will iterate forever and it will check the condition
while(True):
    if(Input=="exit"):
        break
    elif Input.isnumeric():
        print("Number")
    elif Input.isalpha():
        print("Alphabates")
    elif Input.isalnum():
        print("Alphanumeric")
