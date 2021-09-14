String_ = input()
Vowels_Count = 0 
Consonents = 0
Vowels = ['a','e','i','o','u','A','E','I','O','U']
for i in String_:
    if(i in Vowels):
        Vowels_Count += 1
    else:
        Consonents += 1

print("Vowels_Count",Vowels_Count)
print("Consonents+count",Consonents)
