'''Experiment with below statements replacing VAL until all result in True. '''

Input_value= input()

# when we take input as int then only it will print all the true
if Input_value.isnumeric():
    print(isinstance(int(Input_value),int))
    print(isinstance(str(Input_value),str))
    print(isinstance(float(Input_value),float))
else:
    print("It won't print the all the true statements")