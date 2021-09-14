
while(True):
    Input= input()
    if(Input=="exit"):
        break
    elif Input.isnumeric():
        print("Number")
    elif Input.isalpha():
        print("Alphabates")
    elif Input.isalnum():
        print("Alphanumeric")
