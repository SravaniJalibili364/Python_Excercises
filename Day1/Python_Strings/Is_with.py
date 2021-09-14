String = input()
if String.startswith("Is"):
    print(String)
else:
    result = ""
    String = list(String)
    String.append("Is")
    for i in String:
        result = result + i
    print(result)