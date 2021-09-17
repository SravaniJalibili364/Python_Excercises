
'''Write a Python program to get a new string from a given string where "Is" has been added to the front.
 If the given string already begins with "Is" then return the string unchanged.'''


String = input()
#Now checking whether the starting with "Is" or not
if String.startswith("Is") or String.startswith("is"):
    print(String)
else:
    result = ""
    #Is term were stored in the variable
    Is_term = "Is"
    # Now the result ,both is and string will add.
    result = Is_term + String
    print(result)